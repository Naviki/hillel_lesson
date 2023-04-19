import time
class Player:
    def __init__(self):
        self.film_file = None
        self.start_film = None
        self.playing = False
        self.paused = False
        self.quality_level = None
        self.current_time = None
        self.sound = '100'
        self.subtitles = None
        self.audiotrack = 'English'
        self.fullscreen = False


    def play(self, file_path):
        try:
            with open(file_path, 'r') as file:
                # Виконуємо реальне відтворення фільму
                print('Фільм:', file_path, 'відтворено')
                self.film_file = file_path
                self.start_film = time.time()
                self.playing = True
                self.paused = False
                return True
        except FileNotFoundError:
            print('Помилка: Фільм не знайдено')
            return False

    def pause(self):
        if self.playing:
            print('Фільм призупинено')
            self.paused = True
            return True
        else:
            print('Помилка: Фільм не відтворено')
            return False
    def quality(self, quality):
        qualitys = ['360P', '480P', '720P', '1080P']
        if quality not in qualitys:
            print('Помилка: Якість недоступна.')
            return False
        else:
            self.quality_level = quality
            print('Налаштована якість: ', quality)
            return True
    def time_code(self):
        if self.start_film is not None:
            total_time = int(time.time() - self.start_film)
            hours = total_time // 3600
            minutes = (total_time % 3600) // 60
            seconds = total_time % 60
            self.current_time = '{}:{}:{}'.format(hours, minutes, seconds)
            print('Часовий код: {}:{}:{}'.format(hours, minutes, seconds))
            return self.current_time
        else:
            print('Помилка: Фільм не відтворюється')
            return None
    def set_sound(self, volume):
        if 0 <= volume <= 100:
            self.sound = volume
            print('Гучність встановлена: ', volume)
            return True
        else:
            print('Помилка. Недоступна гучність (має бути від 0 до 100)')
            return False
    def subtitles_on(self):
        self.subtitles = True
        print('Субтитри увімкнено')
    def subtitles_off(self):
        self.subtitles = False
        print('Субтитри вимкнено')

    def change_language(self, language):
        languages = ['English', 'Ukrainian', 'Polish', 'France']
        if language not in languages:
            print('Фільм не підтримує цю мову.')
            return False
        else:
            self.audiotrack = language
            print('Мову перегляду змінено на: ', language)
            return True
    def fullscreen_on(self):
        self.fullscreen = True
        print("Фільм на весь екран")
    def fullscreen_off(self):
        self.fullscreen = False
        print("Фільм у віконці")



player = Player()
"""Перевірка методу play"""
file_path = "simpsons.mp4"
file_paths = "sdsdsd.mp4"

player.play(file_paths)
player.play(file_path)

"""Перевірка методу time_code"""
time.sleep(3)
player.time_code()

"""Перевірка методу pause"""
time.sleep(1)
player.pause()

"""Перевірка методу fullscreen_on"""
player.fullscreen_on()
player.fullscreen_off()

"""Перевірка методу change_language"""
player.change_language('Ukrainian')

"""Перевірка методу set_sound"""
player.set_sound(60)

"""Перевірка методу subtitles"""
player.subtitles_on()

"""Перевірка методу quality"""
player.quality('1080P')