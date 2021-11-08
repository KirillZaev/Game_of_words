from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .models import Word


def clear_temp(use_words, last):
    # функция для удобного обнюления игры
    use_words.clear()
    last.clear()
    last.append("123")
    last.append("*")


class InstructionPageView(TemplateView):
    template_name = 'instruction.html'


# переменные для проверки начала игры и прослеживания этапов игры
used_words = []
last_later = ["123", "*"]


def start_game(request):
    # функция для реализации алгоритма подбора слов для игры
    now_word = request.POST['word'].lower()
    now_word = Word.objects.filter(word=now_word)
    my_dict = {}
    if now_word and (last_later[-1] == "*" or
                     (now_word[0].first == last_later[-1] and
                      now_word[0].topic == last_later[-2])):
        if now_word[0].word not in used_words:
            used_words.append(now_word[0].word)
            answer = Word.objects.filter(first=now_word[0].last)
            answer = answer.filter(topic=now_word[0].topic)
            if answer:
                for i in answer:
                    if i.word not in used_words:
                        my_dict = {
                            'word': i
                        }
                        last_later.append(i.topic)
                        last_later.append(i.last)
                        used_words.append(i.word)
                        break
        else:
            my_dict = {
                'word': "Это слово уже было"
            }
    else:
        my_dict = {
            'word': "Это слово не подходит"
        }
    if my_dict:
        return render(request, 'game.html', context=my_dict)
    else:
        my_dict = {
            'word': "Поздравляем вы победили",
            "answer": len(used_words)
        }
        clear_temp(used_words, last_later)
        return render(request, 'win.html', context=my_dict)


class GamePageView(TemplateView):
    template_name = 'game.html'


def lose_game(request):
    clear_temp(used_words, last_later)
    return render(request, 'lose.html')


def topic_game(request):
    clear_temp(used_words, last_later)
    return render(request, 'topic.html')


class AddPageView(CreateView):
    # реализация вкладки добавления нового слова в бд
    template_name = 'add.html'
    model = Word
    fields = '__all__'
