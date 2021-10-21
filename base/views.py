import random
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TechniqueSerializer
from .models import Technique
from .errors import BjjErrors

@api_view(['GET'])
def api_overview(request):
    api_overview = [
        {
            "URLS": {
                'Techniques': '/techniques/all/',
                'Random Technique': '/techniques/any',
                'Techniuqes By Type': '/techniques/type/<str:tech_type>',
                'Techniques By Difficulty': '/techniques/difficulty/<str:difficulty>',
                'Technique By ID': '/techniques/<int:pk>',
                'Technique By Name': '/techniques/name/<str:name>',
                'Techniques By Type And Difficulty': '/techniques/t-d/<str:tech_type>/<str:tech_difficulty>',
                'Create Technique':'/techniques/create/',
                'Update Technique': '/techniques/update/<int:pk>',
                'Delete Technique': '/techniques/delete/<int:pk>'
            },

            "DATA FORMAT": {
                "name": "name",
                "type": ["choke", "sweep", "escape", "joint_lock", "takedown", "mixed"],
                "description": "description",
                "difficulty": ["easy", "intermediate", "advanced"],
                "link": "A valid URL to a video of the technique being displayed."

            }
        }
    ]

    return Response(api_overview)


@api_view(['GET'])
def all_techniques(request):
    """
    Get all techniques currently within the database.
    """
    techs = Technique.objects.all()
    serializer = TechniqueSerializer(techs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def random_technique(request):
    """
    Get a random technique from the database.
    """
    try:
        techs = Technique.objects.all()
        random_tech = random.choice(techs)
    except:
        return Response(BjjErrors.EMPTY)
    serializer = TechniqueSerializer(random_tech)
    return Response(serializer.data)


@api_view(['GET'])
def technique_by_id(request, pk):
    """
    Get a single technique by its ID.
    """
    try:
        tech = Technique.objects.get(id=pk)
        serializer = TechniqueSerializer(tech)
        return Response(serializer.data)
    except: 
        return Response(BjjErrors.ID)


@api_view(['GET'])
def techniques_by_type(request, tech_type):
    """
    Get all techniques under a specific type classification.
    """
    try:
        techs = Technique.objects.all().filter(type=tech_type)
        serializer = TechniqueSerializer(techs, many=True)
        return Response(serializer.data)
    except:
        return Response(BjjErrors.TYPE)


@api_view(['GET'])
def techniques_by_difficulty(request, tech_difficulty):
    """
    Get all techniques under a specific difficulty classification.
    """
    try:
        techs = Technique.objects.all().filter(difficulty=tech_difficulty)
        serializer = TechniqueSerializer(techs, many=True)
        return Response(serializer.data)
    except:
        return Response(BjjErrors.DIFFICULTY)


@api_view(['GET'])
def technique_by_name(request, tech_name):
    """
    Get a technique by its name.
    """
    try:
        tech = Technique.objects.all().filter(name=tech_name)
        serializer = TechniqueSerializer(tech, many=True)
        return Response(serializer.data)
    except:
        return Response(BjjErrors.NAME)


@api_view(['GET'])
def techs_by_type_diff(request, tech_type, tech_difficulty):
    """
    Get all techniques under a set of type and difficulty classifications.
    """
    # Making sure a valid type and difficulty were input.
    if tech_type not in Technique.CHOICES:
        return Response(BjjErrors.TYPE)
    if tech_difficulty not in Technique.CHOICES:
        return Response(BjjErrors.DIFFICULTY)

    techs = Technique.objects.all().filter(type=tech_type, difficulty=tech_difficulty)
    serializer = TechniqueSerializer(techs, many=True)
    return Response(serializer.data)
        

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_technique(request):
    """
    Create a new technique and add it to the database.
    """
    data = request.data

    # These if blocks check that choice options are valid and returns an appropriate response
    # so that the user knows what part of their data was incorrect. 
    if data["type"] not in Technique.CHOICES:
        return Response(BjjErrors.TYPE)
    if data["difficulty"] not in Technique.CHOICES:
        return Response(BjjErrors.DIFFICULTY)

    # Cleaning the name data so that all entries are uniform and easy to search. 
    data["name"] = data["name"].strip().lower().replace(" ", "_")


    # Both choice options are valid, name data cleaned, move on to check if all data is valid.
    serializer = TechniqueSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(BjjErrors.SAVE_FAIL)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def update_technique(request, pk):
    """
    Update a technique that is currently in the database. Select by ID.
    """
    try:
        tech = Technique.objects.get(id=pk)
    except:
        return Response(BjjErrors.ID)

    # Cleaning the name data if the user doesn't stick to normal format.
    data = request.data
    data["name"] = data["name"].strip().lower().replace(" ", "_")

    serializer = TechniqueSerializer(instance=tech, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(BjjErrors.SAVE_FAIL)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_technique(request, pk):
    """
    Delete a technique from the database. Select by ID.
    """
    try:
        tech = Technique.objects.get(id=pk)
    except:
        return Response(BjjErrors.ID)

    tech.delete()
    return Response({"Success": "Technique successfully deleted."})



