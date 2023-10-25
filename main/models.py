from django.conf import settings
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Привычка.
    - Пользователь — создатель привычки.
    - Место — место, в котором необходимо выполнять привычку.
    - Время — время, когда необходимо выполнять привычку.
    - Действие — действие, которое представляет из себя привычка.
    - Признак приятной привычки — привычка,
    которую можно привязать к выполнению полезной привычки.
    - Связанная привычка — привычка, которая связана с другой привычкой,
    важно указывать для полезных привычек,
    но не для приятных.
    - Периодичность (по умолчанию ежедневная) — периодичность
    выполнения привычки для напоминания в днях.
    - Вознаграждение — чем пользователь должен себя вознаградить
    после выполнения.
    - Время на выполнение — время, которое предположительно потратит
    пользователь на выполнение привычки.
    - Признак публичности — привычки можно публиковать в общий доступ,
    чтобы другие пользователи могли брать
    в пример чужие привычки.
    """
    TIMING_CHOICES = (
        ('daily', 'Ежедневно'),
        ('weekly', 'Раз в неделю'),
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

    def clean(self):
        # Вызываем clean для базовой валидации модели
        super().clean()

        # Проверка одновременного выбора связанной
        # привычки и указания вознаграждения
        if self.related_habits and self.reward:
            raise ValidationError(
                "Нельзя одновременно выбирать "
                "связанную привычку и указывать вознаграждение.")

        # Проверка времени выполнения (не больше 120 секунд)
        if self.execution_time and self.execution_time > 120:
            raise ValidationError(
                "Время выполнения не должно превышать 120 секунд.")

        # Проверка связанных привычек: должны быть приятные
        if self.related_habits and not self.related_habits.is_nice:
            raise ValidationError(
                "Связанные привычки могут быть только приятными.")

        # Проверка приятных привычек: не должно быть
        # вознаграждения или связанных привычек
        if self.is_nice and (self.reward or self.related_habits):
            raise ValidationError(
                "У приятных привычек не может быть "
                "вознаграждения или связанных привычек.")

        # Проверка периодичности (не реже 1 раза в 7 дней)
        if self.timing == 'weekly' and self.execution_time < 7 * 24 * 60:
            raise ValidationError(
                "Привычку нельзя выполнять реже, чем 1 раз в 7 дней.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Вызываем валидацию перед сохранением
        super(Habit, self).save(*args, **kwargs)

    def __str__(self):
        return f"привычка {self.action} в {self.location}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
