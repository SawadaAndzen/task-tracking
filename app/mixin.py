from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        Task = self.get_object()
        if Task.user != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)
        

class UserIsCommentOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        Comment = self.get_object()
        if Comment.author != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)