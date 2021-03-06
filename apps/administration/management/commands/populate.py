import string
import datetime
import random
from django.core.management.base import BaseCommand
from apps.accounts.models import Account
from apps.challenges.models import Category, Challenge, Solves, FirstBlood, Flag

categories_list = [
    'web',
    'pwn',
    'crypto',
    'forensic',
    'reversing',
    'recon',
    'misc'
]

usernames_list = [
    'Mad_Thrashers',
    'The_Pace_Makes',
    'Not_Fast_But_furious',
    'Attack_of_the_Invisible Binja',
    'Running_On_Empty',
    'Corporate_Punishment',
    'Club_Win',
    'Big_Dudes_Scared_Shoes',
    'Fifty_Shdes_of_AwesomeVM',
    'Hustle_&_Flow',
    'Game_of_Throjans',
    'Beer_Pressur',
    'Game_of_Throw',
    'Its_Always_Rny_in_Philadelphia',
    'Heres_Johnny',
    'Zombie_Warfare',
    'root',
    'admin',
    'test',
    'guest',
    'info',
    'adm',
    'mysql',
    'user',
    'administrator',
    'oracle',
    'ftp',
    'pi',
    'puppet',
    'ansible',
    'ec2-user',
    'vagrant',
    'azureuser',
]


class Command(BaseCommand):
    help = 'Populates test database with dummy data'

    def add_arguments(self, parser):
        parser.add_argument('team_size', type=int)
        parser.add_argument('chall_size', type=int)
        parser.add_argument('solves_size', type=int)

    def create_teams(self, size):
        for x in range(0, size):
                team_name = random.choice(usernames_list)
                if Account.objects.filter(username=team_name).count() > 0:
                    team_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
                new_account = Account.objects.create(
                    username=team_name,
                    email="{0}@gmail.com".format(team_name),
                )
                new_account.set_password(team_name)
                new_account.save()

    def create_categories(self):
        for category in categories_list:
            if Category.objects.filter(name=category).count() == 0:
                Category.objects.create(
                    name=category,
                )

    def create_challenges(self, size):

        for x in range(0, size):
            new_challenge = Challenge.objects.create(
                category=Category.objects.get(name=random.choice(categories_list)),
                name=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8)),
                description=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + ' ' + string.digits) for _ in range(40)),
                points=''.join(random.choice(string.digits) for _ in range(3))
            )
            new_flag = Flag(
                challenge=new_challenge,
                text="1"
            )
            new_flag.save()

    def create_solves(self, size):
        for x in range(0, size):
            challenge = random.choice(Challenge.objects.all())
            account = random.choice(Account.objects.all())
            random_minutes = random.randint(0, 4000)
            if Solves.objects.filter(account=account, challenge=challenge).count() == 0:
                if Solves.objects.filter(challenge=challenge).count() == 0:
                    FirstBlood.objects.create(
                        account=account,
                        challenge=challenge
                    )
                Solves.objects.create(
                    challenge=challenge,
                    account=account,
                    created_at=datetime.datetime.now() + datetime.timedelta(minutes=random_minutes)
                )

        top_solvers = []
        for x in range(0, 15):
            choice = random.choice(Account.objects.all())
            if choice in top_solvers:
                choice = random.choice(Account.objects.all())
            top_solvers.append(choice)

        for acc in top_solvers:
            for x in range(0, random.randint(0, 10)):
                challenge = random.choice(Challenge.objects.all())
                account = acc
                random_minutes = random.randint(0, 3000)
                Solves.objects.create(
                    challenge=challenge,
                    account=account,
                    created_at=datetime.datetime.now() + datetime.timedelta(minutes=random_minutes)
                )

    def handle(self, *args, **options):
        self.create_categories()
        self.create_teams(options['team_size'])
        self.create_challenges(options['chall_size'])
        self.create_solves(options['solves_size'])
