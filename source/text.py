import pygame
class Text:
    def __init__(self, preferences):
        self._cached_fonts = {}
        self._cached_text = {}
        self.font_preferences = preferences

    def make_font(self,fonts, size):
        available = pygame.font.get_fonts()
        # get_fonts() returns a list of lowercase spaceless font names
        choices = map(lambda x:x.lower().replace(' ', ''), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
        return pygame.font.Font(None, size)

    def get_font(self, size):
        key = str(self.font_preferences) + '|' + str(size)
        font = self._cached_fonts.get(key, None)
        if font == None:
            font = self.make_font(self.font_preferences, size)
            self._cached_fonts[key] = font
        return font
    
    def create_text(self,text, size, color):
        key = '|'.join(map(str, (self.font_preferences, size, color, text)))
        image = self._cached_text.get(key, None)
        if image == None:
            font = self.get_font(size)
            image = font.render(text, True, color)
            self._cached_text[key] = image
        return image

    def draw(self, screen, text):
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
