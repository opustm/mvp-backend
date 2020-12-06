from main.viewsets import CliqueViewset, UserViewset, InvitationViewset, EventViewset, SoloEventViewset, ScheduleViewset, TimeFrameViewset, AnnouncementViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliques', CliqueViewset)
router.register('users', UserViewset)
router.register('invitations', InvitationViewset)
router.register('events', EventViewset)
router.register('soloEvents', SoloEventViewset)
router.register('schedules', ScheduleViewset)
router.register('timeFrames', TimeFrameViewset)
router.register('announcements', AnnouncementViewset)
