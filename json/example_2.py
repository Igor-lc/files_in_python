import json

post = {
    'id': 36,
    'date': 1490764640,
    'likes': {'count': 3},
    'text': 'Здесь  лучшие курсы по Python. '
            'https://t.me/python_django_sql'
            ' Если у вас есть вопросы по практическим заданиям, '
            'то смело задавайте их здесь. '
            'https://t.me/best_python_tasks_for_beginer'
}
print(json.dumps(post, ensure_ascii=False, indent=4))

with open("post.json", "w", encoding="utf-8") as f:
    json.dump(post, f, ensure_ascii=False)
