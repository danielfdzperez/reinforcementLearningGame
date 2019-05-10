import tensorflow as tf
class DDQNs:

    def  __init__(self, name,input_height, input_width, n_hidden_neurons_1, n_hidden_neurons_2, n_outputs):
        self.input_width = input_width
        self.input_height = input_height
        self.n_outputs = n_outputs
        self.name = name

        self.initializer = tf.variance_scaling_initializer()

        #Create the neural network
        with tf.variable_scope(self.name):
            self.input_state = tf.placeholder(tf.float32, shape=[None, input_height, input_width],name='input')
            self.flatten = tf.reshape(self.input_state, shape=[-1, input_width*input_height])

            self.v_s1 = tf.layers.dense(self.flatten, n_hidden_neurons_1, activation = tf.nn.relu, kernel_initializer = self.initializer)
            self.v_s = tf.layers.dense(self.v_s1, n_hidden_neurons_2, activation = tf.nn.relu, kernel_initializer = self.initializer)
            self.value = tf.layers.dense(self.v_s, 1, activation = None, kernel_initializer = self.initializer)

            self.a_sa1 = tf.layers.dense(self.flatten, n_hidden_neurons_1, activation = tf.nn.relu, kernel_initializer = self.initializer)
            self.a_sa = tf.layers.dense(self.a_sa1, n_hidden_neurons_2, activation = tf.nn.relu, kernel_initializer = self.initializer)
            self.advantage = tf.layers.dense(self.a_sa, self.n_outputs, activation = None, kernel_initializer = self.initializer)

            self.outputs = self.value + tf.subtract(self.advantage, tf.reduce_mean(self.advantage, axis=1, keepdims=True))

        with tf.variable_scope(self.name + "Train"):
            self.importance_sampling_weight = tf.placeholder(tf.float32, [None,1])
            self.actions = tf.placeholder(tf.int32, shape=[None])
            self.target_qvalue = tf.placeholder(tf.float32, shape=[None,1])
            self.q_value = tf.reduce_sum(self.outputs * tf.one_hot(self.actions, self.n_outputs),axis=1,keepdims=True)
            
            self.error = tf.abs(self.target_qvalue - self.q_value)
            self.clipped_error = tf.clip_by_value(self.error, 0.0,1.0)
            self.linear_error = 2*(self.error-self.clipped_error)
            self.loss = tf.reduce_mean(self.importance_sampling_weight * (tf.square(self.clipped_error)+self.linear_error))

            self.absolute_errors = tf.abs(self.target_qvalue - self.q_value)
            self.optimizer = tf.train.RMSPropOptimizer(0.00025)
            self.global_step=tf.Variable(0,trainable=False, name="global_step")
            self.training_op = self.optimizer.minimize(self.loss, global_step=self.global_step)

    def update(self,origin_name,sess):
        
        origin = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, origin_name)

        destination = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, self.name)

        ops = []

        for o_var,d_var in zip(origin,destination):
            ops.append(d_var.assign(o_var))

        sess.run(ops)

    def evalAction(self, states):
        return self.outputs.eval(feed_dict={self.input_state:states})

    def evalActionSess(self, states, sess):
        return sess.run(self.outputs,feed_dict={self.input_state:states})


    def train(self,states, actions, q_target,importance_sampling_weight,sess):
        return sess.run([self.training_op, self.loss, self.absolute_errors], 
                        feed_dict={self.input_state: states, self.actions: actions, self.target_qvalue: q_target, 
                            self.importance_sampling_weight: importance_sampling_weight})


    def lossEval(self,states, actions, q_target,sess):
        return sess.run([self.loss], 
                        feed_dict={self.input_state: states, self.actions: actions, self.target_qvalue: q_target})
    def training(self,states, actions, q_target,sess):
        return sess.run([self.training_op], 
                        feed_dict={self.input_state: states, self.actions: actions, self.target_qvalue: q_target})


