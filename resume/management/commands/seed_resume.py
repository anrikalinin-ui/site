from datetime import date

from django.core.management.base import BaseCommand

from resume.models import Profile, Skill, Experience, Education, Project, Metric, Language


class Command(BaseCommand):
    help = 'Заполнить БД демо-данными резюме (Булдыгин Е.А.)'

    def handle(self, *args, **options):
        p, _ = Profile.objects.update_or_create(
            pk=1,
            defaults=dict(
                full_name='Булдыгин Евгений Александрович',
                title='CPO',
                location='Москва',
                bio='Руковожу разработкой продуктов Supply Chain в розничной сети. 11+ лет в '
                    'продуктовой разработке: от системного аналитика до CPO. Построил и веду '
                    'команду из 21 специалиста, управляю бюджетом 300 млн ₽/год.',
                email='evg.buldygin@example.com',
                phone='+7 (906) 777-88-63',
                show_photo=False,
            ),
        )

        exp = [
            dict(
                company='Лемана ПРО (Леруа Мерлен)',
                position='CPO',
                start_date=date(2018, 2, 1),
                end_date=None,
                summary='В зоне ответственности — разработка 3 продуктов и 11 high-critical '
                        'микросервисов Supply Chain: расчёт заказов на пополнение магазинов и '
                        'складов, управление квотами, аналитика снабжения.',
                duties='Разработка и реализация продуктовой стратегии, дорожные карты продуктов\n'
                       'Управление полным жизненным циклом продуктов логистики\n'
                       'Формирование и защита бюджета на уровне C-менеджмента (300 млн ₽/год)\n'
                       'Построение продуктовых метрик: OKR, KPI, сквозная аналитика\n'
                       'Лидирование команд: agile, scrum, Kanban; найм и развитие\n'
                       'Разработка архитектуры продукта (C4 level)\n'
                       'Расчёт юнит-экономики, анализ конкурентной среды',
                results='Автозаказ 90%, снижение упущенного товарооборота компании на 1,2%\n'
                        'CSI пользователей 87%\n'
                        'Экономический эффект микросервисов Replenishment — 228 млн ₽/год\n'
                        'Успешный запуск системы GOLD (Forecast & Replenishment) по всей сети\n'
                        'Онлайн-дашборды склада: утилизация ресурсов выросла на 12%',
            ),
            dict(
                company='ДИКСИ, группа компаний',
                position='Системный аналитик',
                start_date=date(2015, 2, 1),
                end_date=date(2018, 2, 1),
                summary='IT-консалтинг в ГК «Дикси»: внедрение ERP GOLD Central, WMS GOLD Stock '
                        'и разработка собственного ПО. Полный цикл интеграции бизнес-процессов.',
                duties='Presale, сбор требований, описание функциональных требований\n'
                       'Визуализация бизнес-процессов: Visio, BPMN (Bizagi)',
                results='Автоматизация мастер-данных, заказов, приёмки и отгрузки\n'
                        'Внедрение ЕГАИС на всех логистических объектах\n'
                        'Модуль прогнозирования продаж и расчёта автозаказа',
            ),
            dict(
                company='БЕЗАНТ, Торговая компания',
                position='Менеджер по управлению складскими процессами',
                start_date=date(2013, 8, 1),
                end_date=date(2015, 2, 1),
                summary='Управление складским комплексом (20 000 м²) через SAP EWM: от приёмки '
                        'товара до отгрузки клиенту. Участие во внедрении SAP EWM.',
                duties='Управление складскими процессами на базе SAP EWM',
                results='Участие во внедрении SAP EWM в складском комплексе 20 000 м²',
            ),
        ]
        for i, item in enumerate(exp):
            Experience.objects.update_or_create(pk=i + 1, defaults=item)

        edu_higher = [
            dict(year='2014', place='МГТУ им. Н.Э. Баумана, Москва',
                 program='Радиоэлектроника и лазерная техника, Радиоэлектронные системы и устройства'),
        ]
        edu_courses = [
            dict(year='2024', place='Otus', program='Enterprise Architect: архитектура гибкой цифровой'),
            dict(year='2021', place='Product Star', program='Профессия Product Manager'),
            dict(year='2020', place='Skillfactory', program='Тренажёр Product Owner'),
            dict(year='2019', place='Британская высшая школа дизайна', program='Design Thinking'),
            dict(year='2016', place='Дикси', program='BPMN: продвинутый курс'),
        ]
        for i, item in enumerate(edu_higher):
            Education.objects.update_or_create(pk=i + 1, defaults={**item, 'kind': Education.KIND_HIGHER})
        base = len(edu_higher)
        for i, item in enumerate(edu_courses):
            Education.objects.update_or_create(pk=base + i + 1, defaults={**item, 'kind': Education.KIND_COURSE})

        skills = [
            ('Agile', 9), ('Scrum', 8), ('Kanban', 8), ('Продуктовая стратегия', 9),
            ('Управление проектами', 9), ('Управление бюджетом', 9), ('Roadmap', 9),
            ('Бизнес-анализ', 8), ('Unit-экономика', 8), ('Продуктовые метрики', 9),
            ('OKR', 9), ('KPI', 9), ('Управление командой', 9), ('Найм и развитие', 8),
            ('SQL', 6), ('Power BI', 7), ('Miro', 7), ('MS Project', 6), ('Jira', 8),
        ]
        for i, (name, level) in enumerate(skills):
            Skill.objects.update_or_create(pk=i + 1, defaults=dict(name=name, level=level))

        projects = [
            dict(title='GOLD — Forecast & Replenishment',
                 description='Система прогнозирования спроса и автозаказа, запущена по всей сети магазинов. Автозаказ 90%, упущенный товарооборот снижен на 1,2%.',
                 technologies='Supply Chain · Forecasting · Microservices'),
            dict(title='Микросервисы Replenishment',
                 description='Управление ограничениями на заказ и дефицитными запасами. Экономический эффект — 228 млн ₽/год.',
                 technologies='Java · Kafka · PostgreSQL'),
            dict(title='Онлайн-дашборды логистики склада',
                 description='Мониторинг KPI сотрудников в реальном времени. Утилизация ресурсов склада выросла на 12%.',
                 technologies='Power BI · Аналитика'),
            dict(title='ЕГАИС в ГК «Дикси»',
                 description='Внедрение ЕГАИС на всех логистических объектах компании.',
                 technologies='Интеграция · ERP'),
        ]
        for i, item in enumerate(projects):
            Project.objects.update_or_create(pk=i + 1, defaults=item)

        metrics = [
            dict(value='11 лет', label='опыта в продуктовой разработке'),
            dict(value='21', label='специалист в команде'),
            dict(value='300 млн ₽', label='бюджет управления в год'),
            dict(value='90%', label='автозаказ в сети магазинов'),
        ]
        for i, item in enumerate(metrics):
            Metric.objects.update_or_create(pk=i + 1, defaults={**item, 'order': i})

        languages = [
            dict(name='Русский', level='Родной'),
            dict(name='Английский', level='B2 — Средне-продвинутый'),
        ]
        for i, item in enumerate(languages):
            Language.objects.update_or_create(pk=i + 1, defaults=item)

        self.stdout.write(self.style.SUCCESS('Данные заполнены'))
