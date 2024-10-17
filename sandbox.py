from manim import *

class MerkleTreeHowItWorks(Scene):
    def construct(self):
        # Display the title
        title = Text("How Merkle Trees Work", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Display the Merkle Tree structure with placeholders
        leaf_labels = ["h1", "h2", "h3", "h4"]
        leaf_nodes = VGroup()
        leaf_texts = VGroup()
        x_positions = [-5, -2, 2, 5]

        for i, (label, x_pos) in enumerate(zip(leaf_labels, x_positions)):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(DOWN * 2.3 + RIGHT * x_pos)
            text = Text(label).scale(0.6)
            text.move_to(rect.get_center())
            leaf_nodes.add(rect)
            leaf_texts.add(text)

        parent_positions = [-3.5, 3.5]
        parent_nodes = VGroup()
        parent_texts = VGroup()

        for i in range(2):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(UP * 0.5 + DOWN + RIGHT * parent_positions[i])
            text = Text(f"h{i*2+1}{i*2+2}").scale(0.6)
            text.move_to(rect.get_center())
            parent_nodes.add(rect)
            parent_texts.add(text)

        root_node = Square(side_length=1.2, color=ORANGE)
        root_node.shift(UP * 2.3 + DOWN)
        root_text = Text("h1234").scale(0.7)
        root_text.move_to(root_node.get_center())

        # Create arrows
        arrows = VGroup()
        for i in range(2):
            left_arrow = Arrow(start=leaf_nodes[i * 2].get_top() + UP * 0.2, end=parent_nodes[i].get_bottom() + LEFT * 0.3 + DOWN * 0.2, buff=0.1)
            right_arrow = Arrow(start=leaf_nodes[i * 2 + 1].get_top() + UP * 0.2, end=parent_nodes[i].get_bottom() + RIGHT * 0.3 + DOWN * 0.2, buff=0.1)
            arrows.add(left_arrow, right_arrow)

        root_left_arrow = Arrow(start=parent_nodes[0].get_top() + UP * 0.2, end=root_node.get_left() + LEFT * 0.2 +  DOWN * 0.2, buff=0.1)
        root_right_arrow = Arrow(start=parent_nodes[1].get_top()+ UP * 0.2, end=root_node.get_right() + RIGHT * 0.2 +  DOWN * 0.2, buff=0.1)
        arrows.add(root_left_arrow, root_right_arrow)

        # Fade in the entire tree
        self.play(FadeIn(leaf_nodes), FadeIn(leaf_texts), FadeIn(parent_nodes), FadeIn(parent_texts), FadeIn(root_node), FadeIn(root_text), FadeIn(arrows))
        self.wait(1)

        # Highlight how altering any data changes the root hash
        altered_data_text = Text("What if h1 changes?", font_size=28, color=RED)
        altered_data_text.to_edge(DOWN)
        self.play(Write(altered_data_text))
        self.wait(1)

        altered_leaf_text = Text("h1").scale(0.6).move_to(leaf_texts[0].get_center())
        self.play(Transform(leaf_texts[0], altered_leaf_text), leaf_nodes[0].animate.set_color(RED))
        self.wait(1)

        # Show that the root hash changes
        altered_parent_text = Text("h12").scale(0.5).move_to(parent_texts[0].get_center())
        altered_root_text = Text("h1234").scale(0.5).move_to(root_text.get_center())
        self.play(Transform(parent_texts[0], altered_parent_text), parent_nodes[0].animate.set_color(RED))
        self.wait(1)
        self.play(Transform(root_text, altered_root_text), root_node.animate.set_color(RED))
        self.wait(1)

        # Show efficiency in verifying data integrity
        efficiency_text = Text("Merkle Trees efficiently verify data integrity", font_size=28, color=YELLOW)
        efficiency_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(efficiency_text))
        self.wait(3)

if __name__ == "__main__":
    import os
    os.system("manim -qm -p sandbox.py MerkleTreeHowItWorks")