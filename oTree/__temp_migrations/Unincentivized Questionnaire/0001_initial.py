# Generated by Django 2.2.12 on 2021-02-02 01:50

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unincentivized questionnaire_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Unincentivized Questionnaire_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unincentivized questionnaire_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Unincentivized Questionnaire_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='What is your age?')),
                ('gender', otree.db.models.IntegerField(blank=True, choices=[[1, 'Man'], [2, 'Woman'], [3, 'Genderqueer / Non-Binary']], null=True, verbose_name='How do you identify your gender?')),
                ('Student_ID', otree.db.models.StringField(max_length=10000, null=True, verbose_name='What is your student ID number? (you student ID will be used to issue the payment for your participation)')),
                ('high_school_GPA', otree.db.models.FloatField(null=True, verbose_name='What is you high-school total GPA score?')),
                ('SAT', otree.db.models.FloatField(blank=True, null=True, verbose_name='If taken, what is your composite SAT score?')),
                ('ACT', otree.db.models.FloatField(blank=True, null=True, verbose_name='If taken, what is your ACT score?')),
                ('attended_coll', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Have you ever attended college before?')),
                ('transferred', otree.db.models.BooleanField(blank=True, choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Have you transferred from another school?')),
                ('old_school', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='What school did you previously attend?')),
                ('old_school_time', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many semesters have you completed in previous school?(if none, enter 0)')),
                ('t_reason', otree.db.models.IntegerField(blank=True, choices=[[1, 'Financial (Could not afford it)'], [2, 'Practical (Had to move or other reason that made it too difficult to pursue)'], [3, "Interest (Decided it wasn't what I wanted)"], [4, 'Other reason']], null=True, verbose_name='What is the main reason for transferring?')),
                ('not_finishing_reason', otree.db.models.IntegerField(blank=True, choices=[[1, 'I did finish a program'], [2, 'Financial (Could not afford it)'], [3, 'Practical (Had to move or other reason that made it too difficult to pursue)'], [4, "Interest (Decided it wasn't what I wanted)"], [5, 'Other reason']], null=True, verbose_name='What is the main reason for not finishing?')),
                ('t_reason_other', otree.db.models.LongStringField(blank=True, null=True, verbose_name='If you picked "Other reason" , please shortly explain:')),
                ('old_school_started', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many years ago did you first attend college?')),
                ('relationship', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you currently in a relationship?')),
                ('married', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you married?')),
                ('pregnant', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you or your spouse pregnant?')),
                ('has_children', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Do you have children?')),
                ('n_children', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many children do you have')),
                ('house', otree.db.models.IntegerField(choices=[[1, 'Dorms'], [2, 'Rented apartment'], [3, 'Family home']], null=True, verbose_name='Where do you plan to live during this semester?')),
                ('live_parents', otree.db.models.BooleanField(blank=True, choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Do you live with your parent/s?')),
                ('other_people', otree.db.models.IntegerField(blank=True, choices=[[0, 'No'], [1, 'Yes, all my roommates are students'], [2, 'Yes, not all are students']], null=True, verbose_name='Do you live with roommates?')),
                ('other_people_n', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many roommates do you share your home with?')),
                ('local', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Does your family live in Wisconsin?')),
                ('driving_distance', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Do they live within a driving distance away from college?')),
                ('visiting_n', otree.db.models.IntegerField(choices=[[0, 'None'], [1, '1-2 Visits'], [2, 'More than 2 visits']], null=True, verbose_name='How many times do you plan to visit your family per year?')),
                ('calls_n', otree.db.models.IntegerField(choices=[[0, 'Less than once every month'], [1, 'About once every two week'], [2, 'About Once every week'], [3, '2 or 3 times per week'], [4, 'On a daily basis']], null=True, verbose_name='How many times do you usually speak with a family member?')),
                ('calls_l', otree.db.models.IntegerField(choices=[[0, '0-5 minutes'], [1, '6-20 minutes'], [2, 'More than 20 minutes']], null=True, verbose_name='When you speak with a family member, how long is the call, usually?')),
                ('sibs_n', otree.db.models.IntegerField(null=True, verbose_name='How many siblings do you have?')),
                ('sibs_order', otree.db.models.IntegerField(blank=True, choices=[[1, 'Eldest'], [2, 'Middle'], [3, 'Youngest']], null=True, verbose_name='Which are you in the siblings order?')),
                ('sibs_attendance', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many of your siblings attended/ing college?')),
                ('parents_n', otree.db.models.IntegerField(choices=[[0, '0'], [1, '1'], [2, '2'], [3, 'More than two']], null=True, verbose_name='How many parents do you have?')),
                ('parents_edu', otree.db.models.IntegerField(blank=True, choices=[[0, 'Less than high-school'], [1, 'High school diploma or equivalent'], [2, 'Some college, no degree'], [3, "Bachelor's degree"], [4, "Master's degree"], [5, 'Doctoral or professional degree'], [5, "I don't know"]], null=True, verbose_name='What is your parents’ highest completed education level?')),
                ('fam_att_n', otree.db.models.IntegerField(choices=[[0, 'Only me'], [1, 'All the family members above the age 18'], [2, 'At least another family member but me, but not all the family members above the age 18']], null=True, verbose_name='How many of your close family attended college?')),
                ('fam_att_still', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many of them are still attending college?')),
                ('fam_grads', otree.db.models.IntegerField(blank=True, null=True, verbose_name='How many of them graduated college?')),
                ('fam_UWM', otree.db.models.BooleanField(blank=True, choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Do you have a family member who is/was at UWM?')),
                ('current_work', otree.db.models.IntegerField(choices=[[0, 'No'], [1, '1-5 hours per week'], [2, '6-15 hours per week'], [3, '16-25 hours per week'], [4, '26-35 hours per week'], [5, 'More than 35 hours per week']], null=True, verbose_name='Do you currently work? If yes, how many hours per week?')),
                ('main_source', otree.db.models.IntegerField(choices=[[1, 'Personal savings'], [2, 'Family support'], [3, 'Ongoing work'], [4, 'Loan']], null=True, verbose_name='What is your main source of living? That is, the majority of your living expenses and schooling expenditures are covered by:')),
                ('savings', otree.db.models.CurrencyField(null=True, verbose_name='How much money do you have in savings?')),
                ('exp_food', otree.db.models.CurrencyField(null=True, verbose_name='on food (per week)')),
                ('exp_housing', otree.db.models.CurrencyField(null=True, verbose_name='on housing (per week)')),
                ('exp_other', otree.db.models.CurrencyField(null=True, verbose_name='on other expenses (per week)')),
                ('have_enough', otree.db.models.IntegerField(choices=[[0, 'Definitely not'], [1, 'Probably not'], [2, "I don't know"], [3, 'Probably yes'], [4, 'Definitely yes']], null=True, verbose_name='Do you have enough money saved (and/or borrowed) to cover these costs for the coming year at your disposal now?')),
                ('loan', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Did you take a loan to help cover the cost of college?')),
                ('loan_size', otree.db.models.CurrencyField(blank=True, null=True, verbose_name='What is the size of your loan?')),
                ('car', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Do you own a car?')),
                ('car_paid', otree.db.models.BooleanField(blank=True, choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Is it fully paid for?')),
                ('car_left_paid', otree.db.models.CurrencyField(blank=True, null=True, verbose_name='How much do you have left to pay for your car?')),
                ('laptop', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Do you own a laptop?')),
                ('tutoring', otree.db.models.IntegerField(choices=[[1, 'Yes'], [2, "No, I don't need it"], [3, "No, I can't afford it"], [4, "I haven't considered that option"]], null=True, verbose_name='Do you take/intend to take private lessons/paid tutoring while in college?')),
                ('tut_gender', otree.db.models.IntegerField(choices=[[1, 'Not at all important'], [2, 'Slightly important'], [3, 'Important'], [4, 'Very important']], null=True, verbose_name='If you have/were to have a tutor, how important is it to you that your tutor will have the same gender as you?')),
                ('tut_race', otree.db.models.IntegerField(choices=[[1, 'Not at all important'], [2, 'Slightly important'], [3, 'Important'], [4, 'Very important']], null=True, verbose_name='If you have/were to have a tutor, how important is it to you that your tutor will have the same racial background as you?')),
                ('grant', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you a grant recipient?')),
                ('grant_type', otree.db.models.IntegerField(blank=True, choices=[[1, 'Need based'], [2, 'Merit based'], [3, 'Both in the same grant'], [4, 'Both in more than one grant'], [5, 'Other type of grant']], null=True, verbose_name='What type of grant, or on what basis are you receiving it?')),
                ('grant_name', otree.db.models.LongStringField(blank=True, null=True, verbose_name="What is/are the name/s of grants that you are receiving?(If you don't know the name please write the source of the grant, for example, UWM)")),
                ('grant_stigma', otree.db.models.IntegerField(choices=[[1, 'Yes'], [2, 'No'], [3, "I don't know"]], null=True, verbose_name='In you opinion, is there a stigma on need-based grant receiving students?')),
                ('eligible', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you aware of grants which you are eligible to and are not receiving?')),
                ('w_eligible', otree.db.models.IntegerField(blank=True, choices=[[1, 'Merit based'], [2, 'Need based'], [3, 'Both'], [3, 'Other']], null=True, verbose_name='On what basis are you eligible to these grants?')),
                ('not_eligible', otree.db.models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], null=True, verbose_name='Are you aware of grants which you are not eligible to and are not receiving?')),
                ('w_n_eligible', otree.db.models.LongStringField(blank=True, null=True, verbose_name='Which grants are you not eligible for that you know of?')),
                ('finish_exp', otree.db.models.FloatField(null=True, verbose_name='How many years does it take a student to finish college on average?')),
                ('w_c_learn', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to learn new things')),
                ('w_c_salary', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to improve my salary')),
                ('w_c_friends', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to make friends')),
                ('w_c_spouse', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to to meet a spouse')),
                ('w_c_understand', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to understand what I want to do in life')),
                ('w_c_prestige', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='for the prestige')),
                ('w_c_age', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name="because that's just what you do at my age")),
                ('w_c_parents', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='because my parents expect me to')),
                ('w_c_experience', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='for the experience')),
                ('w_c_move', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to postpone working')),
                ('w_c_postpone', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='to move out of home')),
                ('w_c_other', otree.db.models.LongStringField(blank=True, null=True, verbose_name='If there are other important reasons that are not mentioned above, please specify below')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Unincentivized Questionnaire.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unincentivized questionnaire_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unincentivized questionnaire_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unincentivized Questionnaire.Subsession')),
            ],
            options={
                'db_table': 'Unincentivized Questionnaire_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Unincentivized Questionnaire.Subsession'),
        ),
    ]
