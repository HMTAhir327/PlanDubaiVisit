from rest_framework import serializers
from Offers.models import Offers,Slides

SEARCH_PATTERN = ['/media/C%3A/Users/HM%20TAhir/Desktop/faiz%20bhai/PlanDubaiVisit/Backend/static/media/ckeditor/','"/media/ckeditor/']
SITE_DOMAIN = "http://127.0.0.1:8000"
REPLACE_WITH = f'"{SITE_DOMAIN}/media/ckeditor/'

class FixAbsolutePathSerializer(serializers.Field):
    def to_representation(self, value):
        text = ""
        ch = [x for x in SEARCH_PATTERN if x in value]
        # if ch[0]:
        #     print("Found")
        # else:
        #     print("Not Found")
        if value:
            text = value.replace(ch[0], REPLACE_WITH)
        return text

class OfferSerializer(serializers.ModelSerializer):
    # rishTextEditor = FixAbsolutePathSerializer()
    # rishTextEditor = serializers.SerializerMethodField(read_only=True)
    
    # def get_rishTextEditor(self, obj):
    #     value = obj.rishTextEditor
    #     text = ""
    #     ch = [x for x in SEARCH_PATTERN if x in value]
    #     if value:
    #         text = value.replace(ch[0], REPLACE_WITH)
    #     return text

    class Meta:
        model = Offers
        fields = '__all__'

class SlidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slides
        fields = '__all__'