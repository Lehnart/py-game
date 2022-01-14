from engine.esper import Processor
from engine.systems.sound.components import SoundComponent
from engine.systems.sound.events import PlaySoundEvent


class SoundProcessor(Processor):

    def __init__(self):
        pass

    def process(self, *args, **kwargs):

        sound_events = self.world.receive(PlaySoundEvent)

        for sound_event in sound_events:
            if not self.world.entity_exists(sound_event.ent):
                continue

            if not self.world.has_component(sound_event.ent, SoundComponent):
                continue

            sound_component = self.world.component_for_entity(sound_event.ent, SoundComponent)
            if sound_component.sound.get_num_channels() < 1:
                sound_component.sound.play()
