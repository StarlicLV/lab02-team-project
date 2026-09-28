   # Лабораторна робота 02
   
   Набір невеликих Python-утиліт, створений командою в рамках лабораторної роботи №2 «Налаштування середовища розробки та Git workflow».

   Мета проєкту — відпрацювати командну розробку з Git: роботу з гілками, Pull Request, code review, вирішення конфліктів, Issues та випуск релізу.

   ## Інформація про команду
   
   ### Назва команди: ...
   
   ### Учасники команди:
     
   | Учасник | GitHub | Роль | Модуль |
   |---------|--------|------|--------|
   | Систалюк Артем Васильович | [StarlicLV](https://github.com/StarlicLV) | Team lead + ... | назва модуля |
   | Кубський Максим Сергійович | [morgkub](https://github.com/morgkub)) | ... | назва модуля |
   | Марчук Максим Сергійович | [...](https://github.com/...) | ... | назва модуля |

   ## Модулі проєкту

   | Модуль | Файл | Опис | Відповідальний |
   |--------|------|------|----------------|
   | Калькулятор | `calculator.py` | Виконує базові арифметичні операції | ПІБ учасника |
   | Конвертер одиниць | `converter.py` | Переводить величини між одиницями вимірювання | ПІБ учасника |
   | Генератор паролів | `password_generator.py` | Створює випадкові паролі заданої довжини | ПІБ учасника |

   ## Технологічний стек

   - Python 3.10 або новіша версія
   - Git та GitHub
   - Visual Studio Code

   ## Встановлення

   1. Встановіть [Python](https://www.python.org/downloads/) і перевірте версію:
```bash
python --version
```
   2. Встановіть [Git](https://git-scm.com/) і перевірте його:
```bash
git --version
```
   4. Склонуйте репозиторій:
```bash
git clone git@github.com:StarlicLV/lab02-team-project.git
cd lab02-team-project
```
   5. (Необов'язково) Створіть і активуйте віртуальне середовище:
```bash
python -m venv .venv
source .venv/Scripts/activate   # Git Bash на Windows
```
      На macOS та Linux: `source .venv/bin/activate`.
   6. Якщо в проєкті є файл `requirements.txt`, встановіть залежності:
```bash
pip install -r requirements.txt
```

   ## Запуск

   Кожен модуль запускається окремо з кореня репозиторію:

```bash
python calculator.py
python converter.py
python password_generator.py
```

   ## Робота з Git у команді

   Команда працює за моделлю **Feature Branch Workflow**:

   1. Для кожної функції створюється окрема гілка від актуальної `main`:
```bash
git switch main
git pull
git switch -c feature/назва-функції
```
   2. Зміни комітяться за стилем Conventional Commits (`feat:`, `fix:`, `docs:` тощо).
   3. Гілка відправляється на GitHub, і створюється Pull Request.
   4. Після code review та схвалення Pull Request зливається в `main`.
   5. Завдання ведуться в GitHub Issues, а Pull Request посилається на них (`Closes #номер`).

   ## Структура репозиторію

```
lab02-team-project/
├── .gitignore
├── README.md
├── CHANGELOG.md
├── lab02-report.md
├── calculator.py
├── converter.py
└── password_generator.py
```

   ## Історія змін

   Усі зміни описано у файлі [CHANGELOG.md](CHANGELOG.md).
