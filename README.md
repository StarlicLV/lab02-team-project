   # Лабораторна робота 02
   
   Набір невеликих Python-утиліт, створений командою в рамках лабораторної роботи №2 «Налаштування середовища розробки та Git workflow».

   Мета проєкту — відпрацювати командну розробку з Git: роботу з гілками, Pull Request, code review, вирішення конфліктів, Issues та випуск релізу.

   ## Інформація про команду
   
   ### Назва команди: PROGmasters
   
   ### Учасники команди:
     
   | Учасник | GitHub | Роль | Модуль |
   |---------|--------|------|--------|
   | Систалюк Артем Васильович | [StarlicLV](https://github.com/StarlicLV) | Team lead + Dev | Генератор паролів |
   | Кубський Максим Сергійович | [morgkub](https://github.com/morgkub) | Dev + QA | Калькулятор |
   | Марчук Максим Сергійович | [maksymarchuk](https://github.com/maksymarchuk) | Dev + QA | Конвертер одиниць |

   ## Модулі проєкту

   | Модуль | Файл | Опис | Відповідальний |
   |--------|------|------|----------------|
   | Калькулятор | `calculator.py` | Виконує базові арифметичні операції | Кубський Максим Сергійович |
   | Конвертер одиниць | `converter.py` | Переводить величини між одиницями вимірювання | Марчук Максим Сергійович |
   | Генератор паролів | `password_generator.py` | Створює випадкові паролі заданої довжини | Систалюк Артем Васильович |

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

   ## Структура репозиторію

```
lab02-team-project/
├── .gitignore
├── README.md
├── CHANGELOG.md
├── calculator.py
├── converter.py
├── lab02-report.md
└── password_generator.py 
```

   ## Історія змін

   Усі зміни описано у файлі [CHANGELOG.md](CHANGELOG.md).
