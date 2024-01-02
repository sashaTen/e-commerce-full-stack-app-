from    django   import   forms 
from  .models   import   Item


class  NewItemForm(forms.ModelForm):
    class   Meta :
        model =  Item
        fields  =  ('category' ,   'name' ,  'description' ,   'image' ,     'price')




class  EditItem(forms.ModelForm):
    class   Meta :
        model =  Item
        fields  =  ('category' ,   'name' ,  'description' ,   'image' ,     'price')



class    ItemSearchForm(forms.Form):
    search_query  = forms.CharField(max_length=250 ,  required=False, label='Search')



    