from manim import *
TITLE_FONT_SIZE = 50

def create_title(txt):
    return Text(
            txt,
            font_size=TITLE_FONT_SIZE,
            weight=BOLD
        ).to_edge(UP)
class MerkleTreeHowItWorks(Scene):
    def construct(self):
        ########################################
        #         Slide 1: Title Slide

        # Display the company logo
        logo = ImageMobject("img/company_logo.png")
        logo.scale(0.3)
        logo.to_corner(DR)

        slide_1_title = create_title('Understanding Merkle Trees')
        author = Text(
            "Gianlorenzo & Raphael - Renuo Learning Week 2024",
            font_size=25
        ).to_edge(DOWN)
        self.add(slide_1_title, author, logo)
        self.wait(5)

        # Display the subtitle
        subtitle = Text(
            "Ensuring Data Integrity and History",
            color=WHITE,
            font_size=28
        )
        subtitle.next_to(slide_1_title, DOWN, buff=0.5)
        self.play(Write(subtitle))
        self.wait(2)
if __name__ == "__main__":
    import os
    os.system("manim -qm -p sandbox.py MerkleTreeHowItWorks")