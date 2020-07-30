from django.core.management.base import BaseCommand, CommandError
from user.models import UserSubscribeEmail
from substitute.models import Categories, Products
from user.models import CustomUser
from django.core.mail import send_mass_mail
import Pure_butter_web.settings as settings
import random

class Command(BaseCommand):
    help = "cette commande sert à envoyer les emails à toutes les personnes qui se sont inscrites aux newsletter"

    def __init__(self):
        self.list_email = []
        self.list_products = []
        self.list_categories = []
        self.txt = ""
        self.categories = Categories.objects.all()

    def get_email_user_subscribe(self):
        get_email_subscribe = UserSubscribeEmail.objects.all()
        for id_user_subscribe in get_email_subscribe:
            get_email = CustomUser.objects.get(id=id_user_subscribe.id_user.id)
            self.list_email.append(get_email.email)

    def get_random_products(self):
        length_categories = len(self.categories)

        for i in range(3):
            nb_rand = random.randint(1, length_categories)
            get_rand_categories = Categories.objects.get(id=nb_rand)
            products_rand = Products.objects.filter(id_category=get_rand_categories).order_by('score_grade')[:1]
            self.list_products.append(products_rand[0])
            self.list_categories.append(get_rand_categories)

    def text_content(self):
        for i in range(3):
            self.txt += "Venez voir :" + self.list_products[i].product_name + " c'est le meilleur produit de la catégorie " + self.categories[i].name_category + "\n"

    def send_all_email(self, content_msg):
        msg = ('Toujours pleins de substituants chez PureButterWeb', content_msg, settings.env('EMAIL'), self.list_email)
        send_mass_mail((msg, ), fail_silently=False)


    def handle(self, *arg, **options):

        self.get_email_user_subscribe()
        self.get_random_products()
        self.text_content()
        self.send_all_email(self.txt)
