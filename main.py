print("📚 Трекер домашних заданий")
print("=" * 50)

assignments = []

while True:
    print(f"\nЗадание #{len(assignments) + 1}")
    print("-" * 30)

    # Ввод данных
    subject = input("Введите предмет: ").strip()
    if not subject:
        print("❌ Предмет не может быть пустым!")
        continue

    homework = input("Введите домашнее задание: ").strip()
    if not homework:
        print("❌ Домашнее задание не может быть пустым!")
        continue

    status = input("Статус выполнения (сделано/не сделано): ").strip().lower()

    # Определение статуса
    if status in ["сделано", "готово", "выполнено", "да", "yes", "done", "1"]:
        status_display = "✅ Сделано"
    else:
        status_display = "❌ Не сделано"

    assignments.append({
        'subject': subject,
        'homework': homework,
        'status': status_display
    })

    continue_input = input("\nДобавить еще задание? (да/нет): ").strip().lower()
    if continue_input not in ["да", "yes", "д", "y", "1"]:
        break

# Вывод таблицы
if assignments:
    print("\n" + "=" * 90)
    print("📊 ТАБЛИЦА ДОМАШНИХ ЗАДАНИЙ")
    print("=" * 90)
    print(f"{'№':<3} {'Предмет':<15} {'Домашнее задание':<40} {'Статус':<15}")
    print("-" * 90)

    for i, assignment in enumerate(assignments, 1):
        # Обрезаем длинные строки для красивого отображения
        subject = assignment['subject'][:13] + '..' if len(assignment['subject']) > 15 else assignment['subject']
        homework = assignment['homework'][:38] + '..' if len(assignment['homework']) > 40 else assignment['homework']

        print(f"{i:<3} {subject:<15} {homework:<40} {assignment['status']:<15}")

    print("=" * 90)
    print(f"Всего заданий: {len(assignments)}")
else:
    print("\n❌ Не добавлено ни одного задания")

print("\nℹ️ Данные не сохраняются (только вывод на экран)")