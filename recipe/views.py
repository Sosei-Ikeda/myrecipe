from django.shortcuts import render, get_object_or_404
from .models import Recipe

def NoneCheck(text):
    if text == None:
        return ""
    else:
        return text

def index(request):
    menu = NoneCheck(request.GET.get('menu'))
    ingredients = NoneCheck(request.GET.get('ingredient'))
    gen = NoneCheck(request.GET.get('gen'))
    cou = NoneCheck(request.GET.get('cou'))
    dif = NoneCheck(request.GET.get('dif'))
    recipes = Recipe.objects.all()
    if menu != "":
        recipes = recipes.filter(menu__icontains=menu)
    if ingredients != []:
        for ingredient in ingredients.replace('　',' ').split():
            recipes = recipes.filter(ingredient__icontains=ingredient)
    if gen != "":
        recipes = recipes.filter(genre=gen)
    if cou != "":
        recipes = recipes.filter(country=cou)
    if dif != "":
        recipes = recipes.filter(difficulty=dif)
    return render(request, 'recipe/index.html', {'recipes':recipes,
                                                 'menu':menu,
                                                 'ingredient':ingredients,
                                                 'gen':gen,
                                                 'cou':cou,
                                                 'dif':dif,})

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredient.splitlines()
    procedures = recipe.procedure.splitlines()
    return render(request, 'recipe/recipe.html', {'recipe':recipe, 'ingredients':ingredients, 'procedures':procedures})