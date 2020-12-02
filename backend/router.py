from main.viewsets import TeamViewset, UserViewset, InvitationViewset, EventViewset, WeeklyAvailabilityViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('team', TeamViewset)
router.register('user', UserViewset)
router.register('invitation', InvitationViewset)
router.register('event', EventViewset)
router.register('availability', WeeklyAvailabilityViewset)