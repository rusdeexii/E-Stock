from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    อนุญาตแก้ไขได้เฉพาะ admin, ส่วนอื่นอ่านได้อย่างเดียว
    """

    def has_permission(self, request, view):
        # ทุกคนสามารถดู (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # ต้องเป็น admin ถึงแก้ไขได้
        return request.user.is_authenticated and request.user.role == 'admin'
