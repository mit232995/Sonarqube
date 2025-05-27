# mini_access_check.py

# Flask route without auth
@app.route('/user/<id>')
def get_user(id):
    user = User.objects.get(id=id)
    return user.name

# API view without permissions
class UserAPI(APIView):
    def get(self, request, id):
        return User.objects.get(id=id)

# Direct object reference
def update_profile(user_id):
    profile = Profile.objects.get(id=user_id)
    profile.save()
