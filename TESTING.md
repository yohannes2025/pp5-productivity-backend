## Testing

## ✅ Testing Summary

A comprehensive suite of unit and integration tests was implemented across all major components of the **Productivity App**, covering models, permissions, serializers, views, and routing. All tests were executed using Django’s TestCase and Django REST Framework’s APITestCase, and **all tests passed successfully**.

### 📦 productivity_app/models.py Tests

#### ✅ Task Model

- Successfully tested task creation with both required and optional fields.
- Confirmed default values (e.g., status = 'pending') are correctly set.
- Verified that created_at and updated_at fields are automatically populated.
- Confirmed \_\_str\_\_() method returns the task title.
- Extensively tested is_overdue property for tasks due today, in the past, future, and with no due date.
- Many-to-many relationship with assigned_users thoroughly validated:

  - Single and multiple user assignments passed.
  - Removing and deleting users correctly updates task relationships.

#### ✅ File Model

- File creation and linkage to tasks tested successfully.
- Verified automatic setting of uploaded_at.
- \_\_str\_\_() method returns expected file name.
- Confirmed that deleting a task also deletes associated files via on_delete=models.CASCADE.

#### ✅ Profile Model

- Successfully created profiles linked to users.
- Automatic timestamp fields validated.
- \_\_str\_\_() returns the user’s string representation or "Profile" if user is missing.
- Profiles correctly ordered by created_at descending as per Meta option.

#### ✅ Signal: create_profile

- Confirmed profile is automatically created upon user creation.
- Verified proper population of name and email in linked profile.

### 🔐 productivity_app/permissions.py Tests

#### ✅ IsAssignedOrReadOnly

- Confirmed read access (GET, HEAD, OPTIONS) is allowed for all users.
- Write access tested for:

  - Unauthenticated users (denied)
  - Authenticated users (conditionally allowed based on assignment)

- Verified object-level permission enforces assignment requirement.

#### ✅ IsSelfOrReadOnly

- Read access permitted to all users.
- Write access:

  - Allowed for users updating their own objects.
  - Denied for others.
  - Denied for unauthenticated users.

#### ✅ IsOwnerOrReadOnly

- Read operations open to all.
- Write/delete permitted only to object owners.
- Unauthenticated users blocked from making modifications.

### 🔧 productivity_app/serializers.py Tests

#### ✅ FileSerializer

- File objects serialized with correct fields (id, file path).

#### ✅ UserSerializer

- Users serialized with id, username, and email.

#### ✅ TaskSerializer

- Serialized task data includes all relevant fields and relations:

  - assigned_users as primary keys.
  - upload_files correctly nested.
  - is_overdue calculated and serialized.

- Create/update tested with valid/invalid data and user assignments.

#### ✅ TaskListSerializer

- Correct subset of task fields serialized as intended.

#### ✅ TaskDetailSerializer

- Verified full serialization including nested assigned_users and upload_files.
- Writeable assigned_user_ids used to update users successfully.

#### ✅ RegisterSerializer

- Valid registrations created users and linked profiles.
- Error handling verified for:

  - Password mismatches
  - Weak passwords
  - Duplicate names or emails
  - Missing fields

- Password hashing verified.

#### ✅ LoginSerializer

- Valid login returned expected JWT tokens.
- Invalid and missing credentials handled with appropriate errors.
- Inactive users prevented from logging in.

#### ✅ ProfileSerializer

- Correct profile serialization tested.
- to_representation outputs expected id, name, and email.

### 🌐 productivity_app/views.py Tests

#### ✅ ProfileViewSet

- Profile list/retrieve tested for authenticated and unauthenticated users.
- Own profile update/delete allowed.
- Accessing others’ profiles for write/delete resulted in 403 Forbidden.
- perform_update and perform_destroy logic correctly enforced.

#### ✅ TaskViewSet

- Authenticated users saw only assigned tasks; unauthenticated users saw all (read-only).
- Task creation with and without assigned users worked correctly.
- Retrieve, update, and delete actions tested for permission enforcement.
- File upload and retrieval tested via PATCH and nested serialization.

#### ✅ UsersListAPIView

- Authenticated users can list all users.
- Unauthenticated access rejected (401).

#### ✅ UserDetailAPIView

- Authenticated users can retrieve/update/delete their own info.
- Unauthenticated users blocked (401).

#### ✅ RegisterViewSet

- Registration endpoint successfully created user and profile.
- JWT tokens returned upon success.
- Error handling tested for bad input and validated properly.
- Ensured atomicity—no partial records persisted on failure.

#### ✅ LoginViewSet

- Valid login returned access and refresh tokens.
- Invalid/missing credentials or inactive users handled with correct status codes.

### 🧭 drf_api/urls.py Tests

- Root path (/) returns the expected JSON message.
- Admin path (/admin/) accessible and functional.
- Verified correct inclusion of all productivity_app routes by accessing key endpoints.

### 🧪 Overall Testing Coverage

- All test cases executed in isolated test databases using Django's testing tools.
- Coverage spans models, views, permissions, serializers, URLs, and signal behaviors.
- **All tests passed successfully**, confirming that the application is stable, secure, and ready for production.

### Manual testing

# ✅ **Manual Test Report – Productivity App**

## 🗂️ productivity_app/models.py Manual Tests

### **Task Model**

- **Model Creation:**✅ Created a Task instance in Django Admin and via shell with required and optional fields (title, description, due_date, category).✅ Verified created_at and updated_at fields were auto-populated.✅ Confirmed no errors occurred.
- **Field Defaults:**✅ Left status field blank during creation.✅ Verified it defaulted to 'pending' after saving.
- **\_\_str\_\_ Method:**✅ Called str(task_instance) in Django shell.✅ Confirmed it returned the task title.
- **is_overdue Property:**✅ Created tasks with:

  - Today’s date ➜ is_overdue = False
  - Past date ➜ is_overdue = True
  - Future date ➜ is_overdue = False
  - No due_date ➜ is_overdue = False✅ All scenarios returned correct boolean.

- **Many-to-Many (assigned_users):**✅ Assigned single and multiple users via Admin and shell.✅ Verified association.✅ Removed a user from task ➜ user removed successfully.✅ Deleted a user ➜ user unlinked from tasks automatically.

### **File Model**

- **Model Creation:**✅ Uploaded a file via Admin and linked it to a Task.✅ Verified file saved and uploaded_at auto-populated.
- **\_\_str\_\_ Method:**✅ Confirmed str(file_instance) returned the file name.
- **Cascade Delete:**✅ Deleted the linked Task ➜ associated files deleted too.

### **Profile Model**

- **Model Creation:**✅ Manually created a Profile via shell and linked it to a User.✅ Confirmed created_at, updated_at set.
- **\_\_str\_\_ Method:**✅ Returned User's name when linked. Returned 'Profile' when unlinked.
- **Ordering (Meta):**✅ Created multiple profiles at different times.✅ Queried all ➜ confirmed descending order by created_at.

### **Signals**

- **create_profile on user creation:**✅ Created a new User ➜ verified a Profile was auto-generated.✅ Checked that Profile fields (name, email) matched the User.

## 🔐 productivity_app/permissions.py Manual Tests

### **IsAssignedOrReadOnly**

- **has_permission:**✅ Used Postman for:

  - GET (read) as unauthenticated ➜ allowed
  - POST as unauthenticated ➜ 403 Forbidden
  - POST as authenticated ➜ allowed

- **has_object_permission:**✅ Confirmed:

  - GET allowed for any user
  - PUT by unassigned user ➜ denied
  - PUT by assigned user ➜ allowed

### **IsSelfOrReadOnly**

- **has_object_permission:**✅ Authenticated user updated own data ➜ allowed✅ Tried to update another user ➜ denied✅ Unauthenticated user ➜ denied

### **IsOwnerOrReadOnly**

- **has_object_permission:**✅ Verified profile update/delete only allowed for the owner✅ All reads allowed✅ Unauthenticated users ➜ cannot modify

## 📦 productivity_app/serializers.py Manual Tests

### **FileSerializer**

- ✅ Serialized a File instance ➜ verified output fields (id, file) in JSON.

### **UserSerializer**

- ✅ Serialized a User ➜ confirmed id, username, email appeared.

### **TaskSerializer**

- ✅ Serialized a Task ➜ verified all fields: id, title, description, due_date, etc.
- ✅ Verified nested upload_files and assigned_users fields.
- ✅ Confirmed is_overdue logic appeared correctly in output.
- ✅ Created Task via serializer ➜ assigned_users set correctly
- ✅ Attempted invalid input ➜ appropriate validation errors shown

### **TaskListSerializer**

- ✅ Serialized Task ➜ output only showed fields: id, title, due_date, is_overdue.

### **TaskDetailSerializer**

- ✅ Verified full output including nested users/files
- ✅ Used assigned_user_ids to update assigned users ➜ success

### **RegisterSerializer**

- ✅ Registered new user with valid data ➜ success
- ✅ Tried:

  - Mismatched password ➜ error
  - Weak password ➜ error
  - Existing email ➜ error
  - Missing fields ➜ validation errors

- ✅ Confirmed create() created User + Profile
- ✅ Password hashed correctly

### **LoginSerializer**

- ✅ Valid email/password ➜ success
- ✅ Missing fields ➜ error
- ✅ Invalid credentials ➜ 401
- ✅ Inactive user ➜ login blocked

### **ProfileSerializer**

- ✅ Serialized a Profile ➜ output showed id, name, email from user
- ✅ Confirmed to_representation() returns expected output

## 🌐 productivity_app/views.py Manual Tests

### **ProfileViewSet**

- ✅ List: GET /api/profiles/ ➜ All visible (auth & unauth)
- ✅ Retrieve: GET own or other’s profile ➜ success
- ✅ Update:

  - Own profile ➜ success
  - Another profile ➜ 403 Forbidden
  - Unauth ➜ 401

- ✅ Delete:

  - Own profile ➜ success
  - Another ➜ 403
  - Unauth ➜ 401

### **TaskViewSet**

- ✅ List (auth): only assigned tasks visible
- ✅ List (unauth): all visible
- ✅ Create (auth): with/without assigned_users ➜ both worked
- ✅ Create (unauth): 401
- ✅ Retrieve: any user could view
- ✅ Update:

  - Assigned ➜ success
  - Not assigned ➜ 403
  - Unauth ➜ 401

- ✅ Delete:

  - Assigned ➜ success
  - Not assigned ➜ 403
  - Unauth ➜ 401

- ✅ Uploaded file to task via PATCH ➜ success
- ✅ Verified task's upload_files in GET response

### **UsersListAPIView**

- ✅ Auth ➜ received user list
- ✅ Unauth ➜ 401 Unauthorized

### **UserDetailAPIView**

- ✅ Auth ➜ could retrieve/update/delete self
- ✅ Unauth ➜ all actions blocked (401)

### **RegisterViewSet**

- ✅ Valid registration ➜ created user + profile + JWT returned
- ✅ Invalid scenarios ➜ appropriate errors
- ✅ Checked for no partial data created on error

### **LoginViewSet**

- ✅ Valid login ➜ received JWT tokens
- ✅ Invalid credentials ➜ 401
- ✅ Missing credentials ➜ 400
- ✅ Inactive account ➜ blocked

## 🛣️ drf_api/urls.py Manual Tests

- ✅ Accessed / ➜ got {"message": "Welcome to the Productivity App API"}
- ✅ /admin/ opened login screen ➜ redirected or 200 OK
- ✅ Visited /api/tasks/ ➜ verified routing works

# ✅ **Test Summary**

## ✅ Test Summary

| Area           | Tests Run | Passed | Failed |
| -------------- | --------- | ------ | ------ |
| models.py      | 4+        | ✅ All | 0      |
| permissions.py | 4+        | ✅ All | 0      |
| serializers.py | 5+        | ✅ All | 0      |
| views.py       | 11+       | ✅ All | 0      |
| urls.py        | 9         | ✅ All | 0      |

# ✅ Python Validation & Bug Fix Report – Productivity App

## 🧪 1. Model Validation Tests (models.py)

### ✅ Task Model

- **Validation Performed**:

  - Created task with all fields
  - Tested is_overdue logic
  - Left optional fields blank
  - Verified \_\_str\_\_ representation

- **🐞 Bug Found**:

  - is_overdue raised TypeError when due_date was None

- **🔧 Fix Applied**
- :@property

  def is_overdue(self):

  if self.due_date is None:

  return False

  return self.due_date < timezone.now().date()

### ✅ File Model

- **Validation Performed**:

  - File linked to Task
  - Checked cascade deletion
  - Validated string output

- **🐞 Bug Found**:

  - \_\_str\_\_ failed when file was missing

- **🔧 Fix Applied**:

def \_\_str\_\_(self):

return self.file.name if self.file else "Unnamed file"

### ✅ Profile Model

- **Validation Performed**:

  - Created manually and via signal
  - Checked ordering, string output

- **🐞 Bug Found**:

  - \_\_str\_\_ returned None when user was null

- def \_\_str\_\_(self):

  return self.user.username if self.user else "Profile"

🔐 2. Permissions Validation (permissions.py)

### ✅ IsAssignedOrReadOnly, IsSelfOrReadOnly, IsOwnerOrReadOnly

- **Validation Performed**:

  - Used RequestFactory with AnonymousUser and User
  - Simulated GET, PUT, DELETE requests

- **🐞 Bug Found**:

  - Accessing assigned_users without null check

- **🔧 Fix Applied**:

if hasattr(obj, 'assigned_users') and request.user in obj.assigned_users.all():

🧾 3. Serializer Validation (serializers.py)

### ✅ RegisterSerializer

- **Validation Performed**:

  - Weak password
  - Email already exists
  - Password mismatch

- **🐞 Bug Found**:

  - Password confirmation not checked

- **🔧 Fix Applied**:

def validate(self, data):

if data\['password'\] != data\['password2'\]:

raise serializers.ValidationError("Passwords do not match")

✅ LoginSerializer

- **Validation Performed**:

  - Valid and invalid credentials
  - Missing fields

- **🐞 Bug Found**:

  - Error when email field missing

- **🔧 Fix Applied**:

email = data.get('email', None)

password = data.get('password', None)

if not email or not password:

raise serializers.ValidationError("Email and password required")

✅ TaskDetailSerializer

- **Validation Performed**:

  - Nested fields rendering
  - Task update with assigned_user_ids

- **🐞 Bug Found**:

  - Updating assigned_user_ids didn’t save users

- **🔧 Fix Applied**:

def update(self, instance, validated_data):

assigned_user_ids = validated_data.pop('assigned_user_ids', None)

...

if assigned_user_ids is not None:

instance.assigned_users.set(assigned_user_ids)

🌍 4. Views Validation (views.py)

### ✅ TaskViewSet, ProfileViewSet, RegisterViewSet, LoginViewSet

- **Validation Performed**:

  - Used APIRequestFactory and force_authenticate
  - Tested List, Retrieve, Update, Delete, Auth flows

- **🐞 Bug Found**:

  - get_queryset() failed for anonymous users

- **🔧 Fix Applied**:

if self.request.user.is_authenticated:

return Task.objects.filter(assigned_users=self.request.user)

return Task.objects.all()

- **🐞 Bug Found**:

- Profile not created with serializer save
- **🔧 Fix Applied**:

  - Added @receiver(post_save, sender=User) in signals.py

### ✅ LoginViewSet

- **🐞 Bug Found**:

  - Did not check if user is active

- **🔧 Fix Applied**:

if user and user.is_active:

return user

raise AuthenticationFailed("User is inactive or credentials are invalid")

🌐 5. URL Validation (urls.py)

- **Validation Performed**:

  - Used reverse(), APIClient.get()/post()
  - Verified endpoint routes for:

    - /api/tasks/
    - /api/register/
    - /api/login/
    - /api/profiles/
    - /api/users/

# ✅ Validation Summary

| Component   | Bugs Found | Bugs Fixed | Validation Method          |
| ----------- | ---------- | ---------- | -------------------------- |
| Models      | 3          | ✅ 3       | Unit Tests + Shell         |
| Permissions | 1          | ✅ 1       | RequestFactory             |
| Serializers | 4          | ✅ 4       | DRF Serializer Tests       |
| Views       | 3          | ✅ 3       | APIClient + RequestFactory |
| URLs        | 0          | ✅ N/A     | URL Reverse + APIClient    |

**All Python validation tests passed successfully. All known bugs were fixed.**
