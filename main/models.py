from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Привычка.
    - Пользователь — создатель привычки.
    - Место — место, в котором необходимо выполнять привычку.
    - Время — время, когда необходимо выполнять привычку.
    - Действие — действие, которое представляет из себя привычка.
    - Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
    - Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек,
    но не для приятных.
    - Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
    - Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
    - Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
    - Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать
    в пример чужие привычки.
    """
    TIMING_CHOICES = (
        ('daily', 'Ежедневно'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),

    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    location = models.CharField(
        max_length=127,
        verbose_name='место'
    )
    action_time = models.DateTimeField(
        verbose_name='время'
    )
    action = models.CharField(
        max_length=127,
        verbose_name='действие'
    )
    is_nice = models.BooleanField(
        default=False,
        verbose_name='приятная привычка'
    )
    related_habits = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name='связанная привычка'
    )
    timing = models.CharField(
        max_length=127,
        choices=TIMING_CHOICES,
        default='daily',
        verbose_name='периодичность'
    )
    reward = models.CharField(
        max_length=127,
        verbose_name='награда',
        **NULLABLE
    )
    execution_time = models.IntegerField(
        verbose_name='время на выполнение',
        **NULLABLE
    )
    is_publish = models.BooleanField(
        default=False,
        verbose_name='публичность'
    )

    last_completed = models.DateTimeField(
        **NULLABLE,
        verbose_name='последнее выполнение'
    )

    def save(self, *args, **kwargs):
        self.full_clean()  # Вызываем валидацию перед сохранением
        super(Habit, self).save(*args, **kwargs)

    def __str__(self):
        return f"привычка {self.action} в {self.location}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
