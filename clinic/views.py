from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.throttling import UserRateThrottle
from clinic.models import UserProfile, Reception, Visit
from .permissions import IsDoctor
from .serializers import ReceptionSerializer, VisitSerializer
from rest_framework.authtoken.models import Token


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    mobile = request.data["mobile"]
    username = request.data["username"]
    password = request.data["password"]
    national_code = request.data["national_code"]
    if len(UserProfile.objects.filter(mobile__exact=mobile)) == 0:
        userprofile = UserProfile(
            mobile=mobile,
            password=password,
            national_code=national_code
        )
        userprofile.save()
        user = User(
            username=username
        )
        user.save()
        userprofile.user_id = user.id
        userprofile.save()
        Token.objects.create(user=user)
        return Response({"Profile Created!"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"is_user": False}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    mobile = request.data["mobile"]
    password = request.data["password"]
    try:
        userprofile = UserProfile.objects.get(mobile__exact=mobile)
        if userprofile.password == password:
            return Response(data={"Welcome"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"Your Password Incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def log_out(request):
    mobile = request.data["mobile"]
    try:
        user_profile = UserProfile.objects.get(mobile__exact=mobile)
        if user_profile:
            return Response(data={"You Are Logged Out!"}, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response(data={"You Are Not Authenticated"}, status=status.HTTP_404_NOT_FOUND)


class ReceptionViewSet(viewsets.ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(data={"Reception Created!"}, status=status.HTTP_200_OK)
        return Response(data={"Enter Correct data!"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        query_set = Reception.objects.filter(patient_id=user_id).all()
        serializer = self.serializer_class(data=query_set, many=True)
        if serializer.is_valid():
            serializer.list(validated_data=request.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class VisitViewSet(viewsets.ModelViewSet):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={"Dont Created"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        reception_id = request.data['reception_id']
        reception = Reception.objects.get(id=reception_id)
        serializer = self.serializer_class(instance=reception)
        if serializer.is_valid():
            serializer.list(validated_data=request.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={"Dont Created"}, status=status.HTTP_400_BAD_REQUEST)
