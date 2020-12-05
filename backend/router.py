from main.viewsets import TeamViewset, CliqueViewset, UserViewset, InvitationViewset, EventViewset, SoloEventViewset, ScheduleTimeFrameViewset, AnnouncementViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teams', TeamViewset)
router.register('cliques', CliqueViewset)
router.register('users', UserViewset)
router.register('invitations', InvitationViewset)
router.register('events', EventViewset)
router.register('soloEvents', SoloEventViewset)
router.register('scheduleTimeFrames', ScheduleTimeFrameViewset)
router.register('announcements', AnnouncementViewset)
