from manim import *

class MerkleTreeBenefits(Scene):
    def construct(self):
        # Title
        title = Text("Benefits of Merkle Trees", font_size=48, color=TEAL)
        title.to_edge(UP)
        underline = Line(LEFT, RIGHT).next_to(title, DOWN).scale(2).set_color(TEAL)
        self.play(Write(title), Create(underline))
        self.wait(1)

        # Bullet Points with Highlights
        benefits = [
            ("Efficient Data Verification", {"Efficient": YELLOW}),
            ("Data Integrity and Tamper Detection", {"Data Integrity": YELLOW}),
            ("Scalability", {"Scalability": YELLOW}),
            ("Reduced Data Transmission", {"Reduced": YELLOW}),
            ("Efficient Data Synchronization", {"Synchronization": YELLOW}),
            ("Secure Data Structures", {"Secure": YELLOW}),
            ("Versatility in Applications", {"Versatility": YELLOW}),
            ("Supports Simplified Verification Processes", {"Simplified": YELLOW}),
            ("Hierarchical Data Organization", {"Hierarchical": YELLOW}),
            ("Enhances Trust in Distributed Systems", {"Trust": YELLOW}),
        ]

        bullet_points = VGroup()
        for i, (benefit, highlights) in enumerate(benefits):
            bullet = Text(f"• {benefit}", font_size=32, t2c=highlights)
            bullet.align_to(title, LEFT)
            bullet.shift(UP * 1.2 + DOWN * (i * 0.6))
            bullet_points.add(bullet)

        for bullet in bullet_points:
            self.play(Write(bullet))
            self.wait(0.75)

        self.wait(2)

        # Fade out all bullet points and title
        self.play(FadeOut(bullet_points), FadeOut(title), FadeOut(underline))
        self.wait(1)


if __name__ == "__main__":
    import os
    os.system("manim -qm -p benefits.py MerkleTreeBenefits")