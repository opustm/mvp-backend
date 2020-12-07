from main.viewsets import CliqueMessageViewset, RequestViewset, DirectMessageViewset, ReactionViewset, ToDoViewset, CliqueViewset, UserViewset, InvitationViewset, EventViewset, SoloEventViewset, ScheduleViewset, TimeFrameViewset, AnnouncementViewset
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
router.register('cliqueMessages', CliqueMessageViewset)
router.register('directMessages', DirectMessageViewset)
router.register('reactions', ReactionViewset)
router.register('toDos', ToDoViewset)
router.register('requests', RequestViewset)