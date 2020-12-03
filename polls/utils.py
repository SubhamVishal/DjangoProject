from  import Choice, Question

allQuestions = Question.objects.all()

from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()


q.question_text="What's up?"
q.save()

Question.objects.filter(question_text__startswith='What')

from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)
Question.objects.get(pk=1)

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_Set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

c.question

q.choice_set.all()

q.choice_set.count()

q.delete()



python manage.py createsuperuser