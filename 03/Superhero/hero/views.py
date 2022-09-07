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

class SpiderManView(TemplateView):
    template_name = 'hero_template.html'

    def get_context_data(self, **kwargs):
        return {
            'main_image': '/static/assets/img/heroes/spider_man.jpg',
            'hero_name': 'Spider-Man',
            'real_name': 'Peter Parker',
            'about_1': "Peter Benjamin Parker is a former high school student who gained spider-like abilities, fighting crime across New York City as the superhero Spider-Man. While Parker juggled all his continued hero duties with the demands of his high-school life, he was approached by Tony Stark who recruited Spider-Man to join the Avengers Civil War, putting Spider-Man into the brief conflict with his personal hero, Captain America. Parker was given a new suit as well as new Stark technology in exchange for his help, allowing him to return back home to continue his own hero work.\n\nWhile he continued to try and prove himself as a worthy hero in the eyes of Iron Man so he could join the Avengers, Parker began investigating the illicit criminal activities of Vulture, who was attempting to sell his Chitauri based weapons onto the black market. Believing that capturing Vulture would prove his worth as a hero, Spider-Man had decided to go after Vulture alone, with only the assistance of his best friend Ned Leeds, while also trying to win his academic decathlon finals. Eventually, Parker gained the affections of fellow classmate Liz Allan, but learned her father, Adrian Toomes, was Vulture. Spider-Man thwarted Vulture's robbery of a Stark Industries cargo plane, to which Stark showed his respect by offering Parker an official place with the Avengers. Parker turned this down in order to continue being a small-time hero in New York, despite his Aunt May discovering his secret identity.\n\nParker was pulled back into the Avengers' conflict when the Black Order had invaded Earth, joining Stark as a stowaway to rescue Doctor Strange from space. Given a new Iron Spider armor, Parker, Stark and Strange joined forces with the Guardians of the Galaxy, joining their attempts to prevent Thanos from collecting the six Infinity Stones. However, the heroes failed to defeat Thanos during the Battle of Titan, who later fulfilled his goal and initiated the Snap, killing Parker amongst trillions. Having been dead for five years, Spider-Man was resurrected in the Blip, and rejoined their fight against Thanos, ultimately watching Stark sacrifice his life to defeat the Mad Titan.",
            'about_2': "The bereaved and traumatized Parker decided to take some time off his hero duties, seeking refuge on his trip to Europe with all his classmates. However, despite wanting to focus his attention on winning the attention of Michelle Jones, Parker witnessed Hydro-Man's attack in Venice and was recruited by \"Nick Fury\" to work with Mysterio to defeat the Elementals. Dubbed Night Monkey after defeating Molten Man in Prague, Parker bequeathed Stark's glasses to Mysterio, only to discover that Mysterio manipulated him in doing so to gain access to Stark's weaponized drones to stage more threats. Recruiting Happy Hogan's help, Spider-Man traveled to London and defeated Mysterio, who died of a misfired gunshot on the Tower Bridge.\n\nUpon Parker's return to New York, doctored footage was sent to The Daily Bugle incriminating him instead as the mastermind of the drone attacks as well as the murderer of Mysterio, while exposing his true identity to the world in the process. While he was able to escape legal action with defense attorney Matt Murdock, the resulting controversy that upended his and his friends' futures led Parker to enlist Doctor Strange to cast a memory-wiping spell to make the identity of Spider-Man a secret once more. However, Parker's repeated amendments midcasting ruined the spell, resulting in a multiversal rift that unleashed foes of Spider-Man from alternate universes, including Doctor Octopus, Lizard, Electro, Sandman and Norman Osborn. Although intending to cure them before sending them back to avert their ill-fated deaths in their native universes, Osborn's Green Goblin alter convinced the villains to betray Parker, ultimately resulting in his aunt's death. Parker then met two alternate versions of himself who had also been transported alongside their villains to his universe and helped him overcome his grief and cure their enemies in the battle on the Statue of Liberty.\n\nFaced with an impossible choice, Parker had Strange cast another spell to make their universes oblivious to his existence in order to protect the Multiverse from collapsing, erasing himself from his friends and allies memories in his universe. Starting anew, Parker resumed his duties undisturbed as an independent Spider-Man.",
            'about_source': "https://marvelcinematicuniverse.fandom.com/wiki/Spider-Man",
            'quote': '"I really did try to help you. I mean, I could\'ve killed you. At any given moment, but I didn\'t. Because my Aunt May taught me that everyone deserves a second chance."',
            'primary_rgb': '165,19,32'
        }