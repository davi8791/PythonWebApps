from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'body': 'My name is Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'body': 'My name is Tony Stark, but I am Iron Man',
            'image': '/static/images/iron_man.jpg'
        }


class BlackWidow(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'body': 'My name is Natasha Romanova',
            'image': '/static/images/black_widow.jpg'
        }

class ScarletWitchView(TemplateView):
    template_name = 'hero_template.html'

    def get_context_data(self, **kwargs):
        return {
            'main_image': '/static/assets/img/heroes/scarlet_witch.png',
            'hero_name': 'Scarlet Witch',
            'real_name': 'Wanda Maximoff',
            'about_1': "Wanda Maximoff is a native of Sokovia who grew up with her fraternal twin brother, Pietro. Born with the latent mythical ability to harness Chaos Magic, she developed a hatred against Tony Stark and rallied anti-American protests after the Novi Grad Bombings killed her parents. Years later, in an effort to help purge their country of strife, the twins joined HYDRA and agreed to undergo experiments with the Scepter under the supervision of Baron Strucker, with the Mind Stone awakening and amplifying Wanda's powers. While her brother developed super-speed, she attained various psionic abilities. When HYDRA fell, the twins joined Ultron to get their revenge on Stark, but abandoned him when they discovered his true intentions to eradicate humanity. Wanda and Pietro joined the Avengers during the Battle of Sokovia to stop Ultron; Pietro was killed during the battle but Wanda survived, and shortly after relocated to the Avengers Compound in the United States of America.\n\nIn 2016, during the Attack on the IFID Headquarters, Maximoff tried to contain an explosion caused by Crossbones, who pulled the cord on his own explosive vest, but failed in her mission and inadvertently destroyed a nearby building with the blast, killing many of its occupants, much to her horror. Maximoff felt responsible for what happened, and since she was unsure of her decision about the Sokovia Accords, she ended up under Vision's watch, who made every effort to make her feel better. However, Clint Barton convinced her to run away and join Steve Rogers in his fight against Tony Stark's team. As a result of her actions during the Clash of the Avengers and her violation of the Sokovia Accords, Maximoff was briefly imprisoned on the Raft before Rogers freed her alongside her teammates.\n\nOver the next two years, Maximoff reunited and reconciled with Vision, and together the two started living off the grid in Europe, forming a romantic relationship. In 2018, they were ambushed by the Black Order, who sought the Mind Stone, and rejoined the Avengers to seek refuge in Wakanda. Maximoff took part in the city's defence when the Black Order invaded the city, where she was forced to kill Vision to prevent Thanos from completing the Infinity Gauntlet. However, she witnessed Thanos resurrect and kill Vision before initiating the Snap, which claimed Maximoff's life. After the victims of the Snap were resurrected in 2023, Maximoff was among the many heroes who fought during the Battle of Earth, defeating Thanos and his armies.",
            'about_2': "Soon after, Maximoff became overwhelmed by immense grief from her recent personal losses, unwittingly unleashing her Chaos Magic powers to enthrall the citizens of Westview into creating an alternate idyllic paradise of classical sitcom tropes. With a recreated Vision as her husband, Maximoff lived her ideal life, even producing twin sons, Tommy and Billy. Further complicating the crisis was Agatha Harkness, a fellow witch who sought to understand the nature of Maximoff's new reality, and a S.W.O.R.D. operation led by Tyler Hayward who wished to eliminate her. Maximoff, now knowing her own identity as the fabled Scarlet Witch, defeated Harkness and the S.W.O.R.D. agents, and dispelled her reality, erasing her family in the process. As she was now wanted, Maximoff fled into isolation and began studying the Darkhold.\n\nHowever, during her exile, the Darkhold had been slowly corrupting her mind, causing her to believe that the only way for her to see her children again was to find them in a different universe. In her quest to steal the powers of multiversal travel from a teenager called America Chavez, Maximoff came at odds with her former ally Doctor Strange, and massacred members of the Masters of the Mystic Arts as well as a group of superpowered individuals from a different universe known as the Illuminati. Finally, after realizing that her violent rampage caused her to be rejected by the Tommy and Billy from an alternate universe, Maximoff redeemed herself by destroying every version of the Darkhold within the Multiverse and demolishing the Darkhold Castle atop Mount Wundagore, seemingly taking her own life in the process.",
            'about_source': "https://marvelcinematicuniverse.fandom.com/wiki/Scarlet_Witch",
            'quote': '"Look around you. It\'s carved in stone. I was meant to rule everything."',
            'primary_rgb': '196,118,148'
        }