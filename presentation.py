import datetime
import random

from manim import *
from manim_slides import Slide
import hashlib

TITLE_FONT_SIZE = 50

def create_title(txt):
    return Text(
            txt,
            font_size=TITLE_FONT_SIZE,
            weight=BOLD
        ).to_edge(UP)


class MerkleTreePresentation(Slide):
    def construct(self):

        ########################################
        #         Slide 1: Title Slide

        # Display the company logo
        logo = ImageMobject("company_logo.png")
        logo.scale(0.3)
        logo.to_corner(DR)

        slide_1_title = create_title('Understanding Merkle Trees')
        author = Text(
            "Gianlorenzo & Raphael - Renuo Learning Week 2024",
            font_size=25
        ).to_edge(DOWN)
        self.add(slide_1_title, author, logo)
        self.next_slide()

        # Display the subtitle
        subtitle = Text(
            "Ensuring Data Integrity and History",
            color=WHITE,
            font_size=28
        )
        subtitle.next_to(slide_1_title, DOWN, buff=0.5)
        self.play(Write(subtitle))
        self.next_slide()

        # Prepare for the next slide by grouping and fading out
        self.play(FadeOut(subtitle, author))

        ########################################
        #         Slide 2: Agenda

        # Transform the previous title into the new title
        slide_2_title = create_title(
            "Agenda",
        )
        self.play(Transform(slide_1_title, slide_2_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        # Agenda Items
        agenda_items = [
            "1. The Problem Merkle Trees Solve",
            "2. Introduction to Hash Functions",
            "3. What is a Merkle Tree?",
            "4. Example Usages",
            "5. Q&A and Quiz!"
        ]

        # Create Text objects for each item
        agenda_texts = VGroup(
            *[
                Text(
                    item,
                    color=WHITE,

                    font_size=48
                )
                for item in agenda_items
            ]
        )

        # Arrange items vertically with spacing
        agenda_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        agenda_texts.next_to(slide_1_title, DOWN, buff=1)

        # Animate each agenda item fading in sequentially
        for i, item in enumerate(agenda_texts):
            self.play(FadeIn(item), run_time=0.7)
            self.next_slide()

        # Prepare for the next slide
        self.play(FadeOut(agenda_texts))

        ########################################
        #         Slide 3: The Problem Merkle Trees Solve

        # Transform the title
        slide_3_title =  create_title("The Problem")
        self.play(Transform(slide_2_title, slide_3_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        # Main Point
        main_point = Text(
            "\"Ensuring data integrity and tracking history\nin distributed systems.\"",
            color=WHITE,
            font_size=48,
            line_spacing=1
        )
        main_point.next_to(slide_3_title, DOWN, buff=1)
        self.play(FadeIn(main_point, shift=UP * 0.5), run_time=1)
        self.next_slide()

        # Question to Audience
        question = Text(
            "How would you verify that every part of a dataset\nis intact and untampered?",
            color=YELLOW,
            font_size=34,
            line_spacing=1
        )
        question.next_to(main_point, DOWN, buff=1)
        self.play(FadeIn(question, shift=UP * 0.5), run_time=1)
        self.next_slide()

        # Prepare for the next slide
        self.play(FadeOut(main_point), FadeOut(question))

        ########################################
        #         Slide 4/5: Introduction to Hash Functions and visualization

        # Transform the title
        slide_4_title =  create_title("Introduction to Hash Functions")
        self.play(Transform(slide_3_title, slide_4_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        # Question to the audience
        question = Text("Can someone explain what a hash function is?")
        question.next_to(slide_4_title, DOWN, buff=1)
        self.play(Write(question))
        self.next_slide()

        # Display the definition
        definition = Text(
            "A function that converts input data into a fixed-size string of bytes.",
            font_size=36,
            color=YELLOW
        )
        definition.next_to(question, DOWN, buff=0.5)
        self.play(Write(definition))
        self.next_slide()

        # Transition to properties
        self.play(FadeOut(question), FadeOut(definition))

        # Display properties title using Transform
        properties_title = create_title(
            "Properties of Hash Functions"
        )
        self.play(Transform(slide_4_title, properties_title))
        self.next_slide()

        # List of properties
        properties = VGroup(
            Text("1. Deterministic"),
            Text("2. Pre-image Resistance"),
            Text("3. Collision Resistance"),
            Text("4. Fast Computation"),
        ).arrange(DOWN, aligned_edge=LEFT)
        properties.next_to(slide_4_title, DOWN, buff=1)
        self.play(Write(properties))
        self.next_slide()

        # Example illustrating Deterministic property
        self.play(FadeOut(properties))
        prop_title = create_title("1. Deterministic")
        self.play(Transform(slide_4_title, prop_title))
        self.next_slide()

        # Show that same input always produces same output
        input_text1 = Text("Input: 'Hello'")
        input_text1.shift(LEFT * 3 + UP)
        hash_text1 = Text("Hash: 185F8DB3...", font_size=24)
        hash_text1.next_to(input_text1, DOWN)
        self.play(Write(input_text1))
        self.play(Write(hash_text1))
        self.next_slide()

        # Show that input 'Hello' again produces same hash
        input_text2 = Text("Input: 'Hello'")
        input_text2.shift(RIGHT * 3 + UP)
        hash_text2 = Text("Hash: 185F8DB3...", font_size=24)
        hash_text2.next_to(input_text2, DOWN)
        self.play(Write(input_text2))
        self.play(Write(hash_text2))
        self.next_slide()

        # Highlight that hashes are the same
        self.play(Indicate(hash_text1), Indicate(hash_text2))
        self.next_slide()

        # Clean up
        self.play(FadeOut(input_text1), FadeOut(hash_text1),
                  FadeOut(input_text2), FadeOut(hash_text2))
        self.next_slide()

        # Example illustrating Pre-image Resistance
        prop_title_new = create_title("2. Pre-image Resistance")
        self.play(Transform(slide_4_title, prop_title_new))
        self.next_slide()

        # Show given a hash, it's hard to find original input
        given_hash = Text("Given Hash: A9993E36...", font_size=24)
        find_input = Text("Can you find the Input?", color=RED)
        VGroup(given_hash, find_input).arrange(DOWN, buff=0.5).next_to(slide_4_title, DOWN, buff=1)
        self.play(Write(given_hash))
        self.play(Write(find_input))
        self.next_slide()

        # Clean up
        self.play(FadeOut(given_hash), FadeOut(find_input))
        self.next_slide()

        # Example illustrating Collision Resistance
        prop_title_new = create_title("3. Collision Resistance")
        self.play(Transform(slide_4_title, prop_title_new))
        self.next_slide()

        # Improved visualization for Collision Resistance

        # Create multiple inputs and their hashes
        inputs = [
            Text("Input: 'Data1'", font_size=28),
            Text("Input: 'Data2'", font_size=28),
            Text("Input: 'Data3'", font_size=28),
            Text("Input: 'Data4'", font_size=28),
        ]

        # Simulated unique hashes for each input
        hashes = [
            Text("Hash: 5D41402A...", font_size=24, color=ORANGE),
            Text("Hash: 7D793037...", font_size=24, color=ORANGE),
            Text("Hash: 2E997585...", font_size=24, color=ORANGE),
            Text("Hash: 8F14E45F...", font_size=24, color=ORANGE),
        ]
        arrows = []

        # Arrange inputs and hashes vertically
        for i, (inp, hsh) in enumerate(zip(inputs, hashes)):
            inp.shift(LEFT * 3 + UP * (1.5 - i))
            hsh.next_to(inp, RIGHT, buff=2)
            arrow = Arrow(start=inp.get_right(), end=hsh.get_left(), buff=0.1)
            arrows.append(arrow)
            self.play(Write(inp))
            self.play(Create(arrow))
            self.play(Write(hsh))
            self.wait(0.5)

        self.next_slide()
        # Emphasize that all hashes are different
        highlight_rects = [SurroundingRectangle(hsh, color=YELLOW, buff=0.1) for hsh in hashes]
        self.play(*[Create(rect) for rect in highlight_rects])
        self.next_slide()

        # Display a message about collision resistance
        message = Text(
            "Finding two inputs with the same hash is extremely hard!",
            font_size=28,
            color=RED
        )
        message.to_edge(DOWN)
        self.play(Write(message))
        self.next_slide()

        # Clean up the scene
        self.play(
            FadeOut(*inputs),
            FadeOut(*hashes),
            FadeOut(*highlight_rects),
            FadeOut(*arrows),
            FadeOut(message)
        )
        self.next_slide()

        # Example illustrating Fast Computation
        prop_title_new = create_title("4. Fast Computation")
        self.play(Transform(slide_4_title, prop_title_new))
        self.next_slide()

        # Simulate fast computation
        input_large = Text("Input: Large File")
        processing = Text("Processing...", font_size=24)
        hash_large = Text("Hash Computed Instantly!", font_size=24)
        VGroup(input_large, processing, hash_large).arrange(DOWN, buff=0.5).next_to(slide_4_title, DOWN, buff=1)
        self.play(Write(input_large))
        self.play(Write(processing))
        self.wait(0.5)
        self.play(ReplacementTransform(processing, hash_large))
        self.next_slide()

        # Clean up
        self.play(FadeOut(input_large), FadeOut(hash_large))


        # Simple analogy: Fingerprinting data
        analogy_title = create_title("Hash Function as a Digital Fingerprint")
        self.play(Transform(slide_4_title, analogy_title))
        self.next_slide()

        # Visualize data and its 'fingerprint'
        data = Text("Data")
        fingerprint = Text("Unique Fingerprint (Hash)", color=YELLOW)
        arrow = Arrow(start=data.get_bottom(), end=fingerprint.get_top(), buff=0.1)
        VGroup(data, arrow, fingerprint).arrange(DOWN, buff=0.5).next_to(slide_4_title, DOWN, buff=1)
        self.play(Write(data))
        self.play(Create(arrow))
        self.play(Write(fingerprint))
        self.next_slide()

        # Clean up
        self.play(FadeOut(data), FadeOut(arrow), FadeOut(fingerprint))
        self.next_slide()

        ########################################
        #         Slide 6: Building Blocks of Merkle Trees

        # Transform the title
        slide_6_title =  create_title("Building Blocks of Merkle Trees")
        self.play(Transform(slide_4_title, slide_6_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        slide_6_tiles = []


        # Step 1: Display data blocks (leaf nodes)
        leaf_labels = ["D1", "D2", "D3", "D4"]
        leaf_nodes = VGroup()
        leaf_texts = VGroup()

        # Define positions for leaf
        x_positions = [-5, -2, 2, 5]

        for i, (label, x_pos) in enumerate(zip(leaf_labels, x_positions)):
            # Create a rectangle for the data block (leaf node)
            rect = Square(side_length=1.0)
            rect.shift(DOWN * 2 + RIGHT * x_pos)
            # Add label to the rectangle
            text = Text(label).scale(0.6)
            text.move_to(rect.get_center())
            # Add to groups
            leaf_nodes.add(rect)
            leaf_texts.add(text)
            # Animate creation
            self.play(Create(rect), Write(text))
            self.wait(0.5)

        self.next_slide()

        # Step 2: Transform data blocks into hash nodes
        hash_nodes = VGroup()
        hash_texts = VGroup()

        for i in range(4):
            # Transform the data block into a hash node with an orange border
            hash_rect = Square(side_length=1.0, color=ORANGE)
            hash_rect.move_to(leaf_nodes[i].get_center())
            hash_label = Text(f"h{i + 1}").scale(0.6)
            hash_label.move_to(hash_rect.get_center())

            # Add to groups
            hash_nodes.add(hash_rect)
            hash_texts.add(hash_label)

            slide_6_tiles.append(leaf_nodes[i])
            slide_6_tiles.append(leaf_texts[i])

            # Animate the transformation
            self.play(Transform(leaf_nodes[i], hash_rect), Transform(leaf_texts[i], hash_label))
            self.wait(0.5)

        self.next_slide()

        # Step 3: Combine hashes to form parent hashes
        parent_hash_nodes = VGroup()
        parent_hash_texts = VGroup()
        arrows_to_parents = VGroup()

        # Define positions for parent hashes, placing them symmetrically
        parent_positions = [-3.5, 3.5]

        for i in range(2):
            # Create copies of hash nodes to move together towards the parent
            left_child_copy = hash_texts[i * 2].copy()
            right_child_copy = hash_texts[i * 2 + 1].copy()

            # Create parent concatenated node
            rect = Square(side_length=1.2, color=WHITE)
            rect.shift(UP * 1 + DOWN + RIGHT * parent_positions[i])

            # Arrows from child hashes to parent, shorter with space at the ends
            left_child = hash_nodes[i * 2]
            right_child = hash_nodes[i * 2 + 1]
            left_arrow = Arrow(
                start=left_child.get_top() + UP * 0.1,
                end=rect.get_bottom() + LEFT * 0.1 + DOWN * 0.1,
                buff=0.1
            )
            right_arrow = Arrow(
                start=right_child.get_top() + UP * 0.1,
                end=rect.get_bottom() + RIGHT * 0.1 + DOWN * 0.1,
                buff=0.1
            )
            arrows_to_parents.add(left_arrow, right_arrow)
            # Add to groups
            parent_hash_nodes.add(rect)
            label = VGroup(left_child_copy, right_child_copy)
            parent_hash_texts.add(label)

            # Animate concatenation and hashing
            self.play(Create(left_arrow), Create(right_arrow))
            self.wait(0.5)

            self.play(left_child_copy.animate.move_to(RIGHT * (parent_positions[i] - 0.2)),
                      right_child_copy.animate.move_to(RIGHT * (parent_positions[i] + 0.2)))
            self.wait(0.5)

            self.play(Create(rect))

            slide_6_tiles.append(left_arrow)
            slide_6_tiles.append(right_arrow)

            self.next_slide()

        self.next_slide()

        for i in range(2):
            # Transform the data block into a hash node with an orange border
            hash_rect = Square(side_length=1.0, color=ORANGE)
            hash_rect.move_to(parent_hash_nodes[i].get_center())
            hash_label = Text(f"h{i * 2 + 1}{i * 2 + 2}").scale(0.6)
            hash_label.move_to(hash_rect.get_center())

            # Add to groups
            hash_nodes.add(hash_rect)
            hash_texts.add(hash_label)
            slide_6_tiles.append(parent_hash_nodes[i])
            slide_6_tiles.append(parent_hash_texts[i])

            # Animate the transformation
            self.play(Transform(parent_hash_nodes[i], hash_rect), Transform(parent_hash_texts[i], hash_label))
            parent_hash_nodes[i] = hash_rect
            parent_hash_texts[i] = hash_label

            self.wait(0.5)

        self.next_slide()

        # Step 4: Combine parent hashes to form the root hash
        root_node = Square(side_length=1.5, color=WHITE)
        root_node.shift(UP * 3 + DOWN)

        # Arrows from parent hashes to root hash, shorter with space between boxes and arrow tips
        left_parent = parent_hash_nodes[0]
        right_parent = parent_hash_nodes[1]
        left_arrow = Arrow(
            start=left_parent.get_top() + UP * 0.1,
            end=root_node.get_bottom() + LEFT * 0.05 + DOWN * 0.2,
            buff=0.1
        )
        right_arrow = Arrow(
            start=right_parent.get_top() + UP * 0.1,
            end=root_node.get_bottom() + RIGHT * 0.05 + DOWN * 0.2,
            buff=0.1
        )
        slide_6_tiles.append(left_arrow)
        slide_6_tiles.append(right_arrow)

        # Animate concatenation and hashing for root
        left_parent_copy = parent_hash_texts[0].copy()
        right_parent_copy = parent_hash_texts[1].copy()
        self.play(Create(left_arrow), Create(right_arrow))
        self.wait(0.5)

        self.play(left_parent_copy.animate.move_to(UP * 3 + DOWN + LEFT * 0.3),
                  right_parent_copy.animate.move_to(UP * 3 + DOWN + RIGHT * 0.3))

        root_text = VGroup(left_parent_copy, right_parent_copy)

        self.wait(0.5)
        self.play(Create(root_node))
        self.next_slide()

        # Transform the data block into a hash node with an orange border
        root_hash_node = Square(side_length=1.5, color=ORANGE)
        root_hash_node.shift(UP * 3 + DOWN)
        root_hash_text = Text("h1234").scale(0.7)
        root_hash_text.move_to(root_node.get_center())

        # Add to groups
        hash_nodes.add(root_hash_node)
        hash_texts.add(root_hash_text)

        # Animate the transformation
        self.play(Transform(root_node, root_hash_node), Transform(root_text, root_hash_text))
        slide_6_tiles.append(root_node)
        slide_6_tiles.append(root_text)

        # Prepare for the next slide
        self.next_slide()
        self.play(FadeOut(*slide_6_tiles))

        ########################################
        #         Slide 7: What is a Merkle Tree?

        # Transform the title
        slide_7_title =  create_title("What is a Merkle Tree? ")
        self.play(Transform(slide_6_title, slide_7_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        # Display the definition of a Merkle Tree
        definition_lines = [
            "A tree where:",
            "1. Every leaf node is a hash of data",
            "2. Every non-leaf node is a hash of its children"
        ]
        definition = VGroup(*[Text(line, font_size=30) for line in definition_lines]).arrange(DOWN, aligned_edge=LEFT,
                                                                                              buff=0.3)
        definition.next_to(slide_7_title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.next_slide()

        # Show a Merkle Tree diagram focusing on two layers at a time
        leaf_labels = ["1", "2", "3", "4"]
        leaf_nodes = VGroup()
        leaf_texts = VGroup()
        x_positions = [-5, -2, 2, 5]

        slide_7_tiles = []


        for i, (label, x_pos) in enumerate(zip(leaf_labels, x_positions)):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(DOWN * 2 + RIGHT * x_pos)
            text = Text(f"h{label}").scale(0.6)
            text.move_to(rect.get_center())
            leaf_nodes.add(rect)
            leaf_texts.add(text)
            slide_7_tiles.append(rect)
            slide_7_tiles.append(text)
            self.play(Create(rect), Write(text))
            self.wait(0.5)

        self.next_slide()

        parent_positions = [-3.5, 3.5]
        parent_nodes = VGroup()
        parent_texts = VGroup()
        parent_arrows = VGroup()
        for i in range(2):
            rect = Square(side_length=1.2, color=ORANGE)
            rect.shift(UP * 0.5 + DOWN + RIGHT * parent_positions[i])
            text = Text(f"h{i * 2 + 1}{i * 2 + 2}").scale(0.6)
            text.move_to(rect.get_center())
            parent_nodes.add(rect)
            parent_texts.add(text)
            left_arrow = Arrow(start=leaf_nodes[i * 2].get_top(), end=rect.get_bottom() + LEFT * 0.3, buff=0.1)
            right_arrow = Arrow(start=leaf_nodes[i * 2 + 1].get_top(), end=rect.get_bottom() + RIGHT * 0.3, buff=0.1)
            slide_7_tiles.append(left_arrow)
            slide_7_tiles.append(right_arrow)
            slide_7_tiles.append(rect)
            slide_7_tiles.append(text)
            parent_arrows.add(left_arrow, right_arrow)
            self.play(Create(left_arrow), Create(right_arrow))
            self.play(Create(rect), Write(text))
            self.wait(0.5)

        self.next_slide()

        # Shift everything down before showing the root node
        self.play(leaf_nodes.animate.shift(DOWN * 1.5), leaf_texts.animate.shift(DOWN * 1.5),
                  parent_nodes.animate.shift(DOWN * 1.5), parent_texts.animate.shift(DOWN * 1.5),
                  parent_arrows.animate.shift(DOWN * 1.5)
                  )

        self.next_slide()

        # Step 3: Display the root node (hD1D2D3D4)
        root_node = Square(side_length=1.5, color=ORANGE)
        root_text = Text("h1234").scale(0.6)
        root_text.move_to(root_node.get_center())

        left_arrow = Arrow(start=parent_nodes[0].get_top() + UP * 0.2,
                           end=root_node.get_bottom() + LEFT * 0.2 + DOWN * 0.2, buff=0.1)
        right_arrow = Arrow(start=parent_nodes[1].get_top() + UP * 0.2,
                            end=root_node.get_bottom() + RIGHT * 0.2 + DOWN * 0.2, buff=0.1)
        slide_7_tiles.append(left_arrow)
        slide_7_tiles.append(right_arrow)
        slide_7_tiles.append(root_node)
        slide_7_tiles.append(root_text)
        self.play(Create(left_arrow), Create(right_arrow))
        self.play(Create(root_node), Write(root_text))
        self.next_slide()

        self.play(FadeOut(definition))
        self.next_slide()

        # Emphasize the root hash as the summary of all data
        emphasize_text = Text("The Root Hash summarizes all data in the tree", font_size=28, color=YELLOW)
        emphasize_text.next_to(root_node, UP, buff=1)
        slide_7_tiles.append(emphasize_text)
        arrow_to_root = Arrow(start=emphasize_text.get_bottom(), end=root_node.get_top(), buff=0.2, color=YELLOW)
        slide_7_tiles.append(arrow_to_root)
        self.play(Write(emphasize_text), Create(arrow_to_root))
        self.next_slide()
        self.play(FadeOut(*slide_7_tiles))

        self.next_slide()

        ########################################
        #         Slide 8: How Merkle Trees Work

        # Transform the title
        slide_8_title =  create_title("How Merkle Trees Work")
        self.play(Transform(slide_7_title, slide_8_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        # Step 1: Display the Merkle Tree structure with placeholders
        leaf_labels = ["h1", "h2", "h3", "h4"]
        leaf_nodes = VGroup()
        leaf_texts = VGroup()
        x_positions = [-5, -2, 2, 5]

        slide_8_tiles = []

        for i, (label, x_pos) in enumerate(zip(leaf_labels, x_positions)):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(DOWN * 2.3 + RIGHT * x_pos)
            text = Text(label).scale(0.6)
            text.move_to(rect.get_center())
            leaf_nodes.add(rect)
            leaf_texts.add(text)
            slide_8_tiles.append(rect)
            slide_8_tiles.append(text)

        parent_positions = [-3.5, 3.5]
        parent_nodes = VGroup()
        parent_texts = VGroup()

        for i in range(2):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(UP * 0.5 + DOWN + RIGHT * parent_positions[i])
            text = Text(f"h{i * 2 + 1}{i * 2 + 2}").scale(0.6)
            text.move_to(rect.get_center())
            parent_nodes.add(rect)
            parent_texts.add(text)
            slide_8_tiles.append(rect)
            slide_8_tiles.append(text)

        root_node = Square(side_length=1.2, color=ORANGE)
        root_node.shift(UP * 2.3 + DOWN)
        root_text = Text("h1234").scale(0.6)
        root_text.move_to(root_node.get_center())
        slide_8_tiles.append(root_node)
        slide_8_tiles.append(root_text)

        # Create arrows
        arrows = VGroup()
        for i in range(2):
            left_arrow = Arrow(start=leaf_nodes[i * 2].get_top() + UP * 0.2,
                               end=parent_nodes[i].get_bottom() + LEFT * 0.3 + DOWN * 0.2, buff=0.1)
            right_arrow = Arrow(start=leaf_nodes[i * 2 + 1].get_top() + UP * 0.2,
                                end=parent_nodes[i].get_bottom() + RIGHT * 0.3 + DOWN * 0.2, buff=0.1)
            arrows.add(left_arrow, right_arrow)
            slide_8_tiles.append(left_arrow)
            slide_8_tiles.append(right_arrow)

        root_left_arrow = Arrow(start=parent_nodes[0].get_top() + UP * 0.2,
                                end=root_node.get_left() + LEFT * 0.2 + DOWN * 0.2, buff=0.1)
        root_right_arrow = Arrow(start=parent_nodes[1].get_top() + UP * 0.2,
                                 end=root_node.get_right() + RIGHT * 0.2 + DOWN * 0.2, buff=0.1)
        arrows.add(root_left_arrow, root_right_arrow)
        slide_8_tiles.append(root_left_arrow)
        slide_8_tiles.append(root_right_arrow)

        # Fade in the entire tree
        self.play(FadeIn(leaf_nodes), FadeIn(leaf_texts), FadeIn(parent_nodes), FadeIn(parent_texts), FadeIn(root_node),
                  FadeIn(root_text), FadeIn(arrows))
        self.next_slide()

        # Highlight how altering any data changes the root hash
        altered_data_text = Text("What if h1 changes?", font_size=25)
        altered_data_text.to_edge(DOWN)
        self.play(Write(altered_data_text))
        self.next_slide()

        altered_leaf_text = Text("h1").scale(0.6).move_to(leaf_texts[0].get_center())
        self.play(Transform(leaf_texts[0], altered_leaf_text), leaf_nodes[0].animate.set_color(BLUE))
        self.next_slide()

        # Show that the root hash changes
        altered_parent_text = Text("h12").scale(0.5).move_to(parent_texts[0].get_center())
        altered_root_text = Text("h1234").scale(0.5).move_to(root_text.get_center())
        self.play(Transform(parent_texts[0], altered_parent_text), parent_nodes[0].animate.set_color(BLUE))
        self.next_slide()
        self.play(Transform(root_text, altered_root_text), root_node.animate.set_color(BLUE))
        self.next_slide()

        # Show efficiency in verifying data integrity
        efficiency_text = Text("Merkle Trees efficiently verify data integrity", font_size=28, color=YELLOW)
        efficiency_text.next_to(slide_8_title, DOWN, buff=0.5)
        self.play(Write(efficiency_text))
        self.next_slide()
        self.play(FadeOut(efficiency_text), FadeOut(*slide_8_tiles), FadeOut(altered_data_text))

        ########################################
        #         Slide 9: Example Usage - BitTorrent

        # Transform the title
        slide_9_title =  create_title("Example Usage - BitTorrent")
        self.play(Transform(slide_8_title, slide_9_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        label_1 = Text("1. Retrieve file metadata", font_size=25).to_edge(DOWN)
        self.play(Write(label_1))

        # Animation 1: Large File with a Hash
        file_box = Square().scale(1.5).set_fill(BLUE, opacity=0.5)
        file_label = Text("File.mkv 30GB").next_to(file_box, UP)
        file_hash_text = Text("Merkle Root:", color=BLUE).next_to(file_box, DOWN + LEFT)
        file_hash_hash = Text("f2f5f5426").next_to(file_hash_text, RIGHT, buff=0.2)
        file_hash = VGroup(file_hash_text, file_hash_hash)
        self.play(Create(file_box), Write(file_label), Write(file_hash))
        self.next_slide()

        label_2 = Text("2. Get chunks from seeds", font_size=25).to_edge(DOWN)
        self.play(ReplacementTransform(label_1, label_2))
        self.next_slide()


        chunks = VGroup(*[Square().scale(0.5).set_fill(BLUE, opacity=0.5) for _ in range(4)])
        chunks.arrange_in_grid(rows=1, buff=0.5).next_to(slide_9_title, DOWN, buff=2)

        chunk_labels = VGroup(*[Text(f"C{i+1}").next_to(chunks[i], DOWN) for i in range(4)])

        self.play(ReplacementTransform(file_box, chunks), Write(chunk_labels), FadeOut(file_label), FadeOut(file_hash))
        self.next_slide()

        label_3 = Text("3. Download Chunks", font_size=25).to_edge(DOWN)
        self.play(ReplacementTransform(label_2, label_3))
        self.next_slide()

        chunk_hashes = VGroup(*[Text(f"H{i+1}").next_to(chunks[i], DOWN).set_color(ORANGE) for i in range(4)])

        for i in [3, 0, 2, 1]:
            self.play(chunks[i].animate.set_fill(GREEN, opacity=0.7), run_time=1)
            self.wait(0.2)

        self.next_slide()

        label_4 = Text("4. Compute Merkle Tree", font_size=25).to_edge(DOWN)
        self.play(ReplacementTransform(label_3, label_4))
        self.next_slide()

        for i in range(4):
            self.play(chunks[i].animate.set_fill(ORANGE, opacity=0.7), run_time=1)
            self.play(ReplacementTransform(chunk_labels[i], chunk_hashes[i]))

        self.next_slide()

        merkle_root_text = Text("H1234:", color=ORANGE).move_to(ORIGIN + LEFT)
        self.play(ReplacementTransform(chunks, merkle_root_text), FadeOut(chunk_hashes))
        self.next_slide()

        merkle_root_hash = Text("f2f5f5426").next_to(merkle_root_text, RIGHT)
        merkle_root_group = VGroup(merkle_root_text, merkle_root_hash)
        self.play(Write(merkle_root_hash))
        self.next_slide()


        label_5 = Text("5. Compare Root Hash", font_size=25).to_edge(DOWN)
        self.play(ReplacementTransform(label_4, label_5))
        self.next_slide()

        file_text = Text("File Merkle Root:", color=BLUE).next_to(merkle_root_text, DOWN)
        file_hash = Text("f2f5f5426").next_to(file_text, RIGHT)
        file_text_group = VGroup(file_text, file_hash)

        self.play(Write(file_text_group))
        self.next_slide()

        label_6 = Text("File Integrity Verified!", color=GREEN).to_edge(DOWN)
        self.play(Indicate(file_hash, scale_factor=1.2, color=GREEN), Indicate(merkle_root_hash, scale_factor=1.2, color=GREEN))
        self.play(ReplacementTransform(label_5, label_6))
        self.next_slide()

        # Clear the scene
        self.play(FadeOut(VGroup(merkle_root_group, file_text_group, label_6)))

        # ########################################
        # #         Slide 10: Example Usage - Git
        #
        # # Transform the title
        # slide_10_title =  create_title("Example Usage - Git")
        # self.play(Transform(slide_9_title, slide_10_title, replace_mobject_with_target_in_scene=True))
        # self.next_slide()

        ########################################
        #         Slide 11: Example Usage - BitCoin

        # Transform the title
        slide_11_title =  create_title("Example Usage - Bitcoin")
        self.play(Transform(slide_9_title, slide_11_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        # Create a block representing a container labeled "Bitcoin Block"
        bitcoin_block = Rectangle(width=6, height=4).set_fill(BLUE, opacity=0.3)
        block_label = Text("Bitcoin Block", font_size=24).next_to(bitcoin_block, UP)
        self.play(Create(bitcoin_block), Write(block_label))
        self.next_slide()

        # Create a matrix of transactions inside the block
        transactions = VGroup(*[Text(f"Tx {i + 1}", font_size=20) for i in range(16)])
        transactions.arrange_in_grid(rows=4, buff=0.7).move_to(bitcoin_block.get_center())
        self.play(ShowIncreasingSubsets(transactions), run_time=4)
        self.next_slide()

        transaction_hashes = VGroup()
        for i in range(16):
            tx_hash = hashlib.sha256(f"Tx {i + 1}".encode()).hexdigest()[:5]
            hash_text = Text(f"{tx_hash}..", font_size=20, color=ORANGE)
            transaction_hashes.add(hash_text)
        transaction_hashes.arrange_in_grid(rows=4, buff=0.7).move_to(bitcoin_block.get_center())
        self.play(ReplacementTransform(transactions, transaction_hashes))
        self.next_slide()

        combined_hash_input = ''.join([hashlib.sha256(f"Tx {i + 1}".encode()).hexdigest() for i in range(16)])
        merkle_root_hash = hashlib.sha256(combined_hash_input.encode()).hexdigest()[:15]
        merkle_root = Text(f"Root Hash: {merkle_root_hash}...", font_size=25, color=ORANGE).move_to(bitcoin_block.get_center())
        self.play(ReplacementTransform(transaction_hashes, merkle_root))
        self.next_slide()

        # Add text explaining the Merkle root
        explanation_1 = Text("Merkle root summarizes all the transactions in a block", font_size=25).to_edge(DOWN)
        self.play(Write(explanation_1))
        self.next_slide()

        # Add basic information below the block after explanation
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prev_block_hash = hashlib.sha256("Previous Block".encode()).hexdigest()[:15] + "..."
        prev_block_time = Text(f"Timestamp: {timestamp}", font_size=25).next_to(merkle_root, DOWN, buff=0.3)
        block_info = VGroup(prev_block_time, merkle_root)

        explanation_2_1 = Text("Blocks contain other important information like timestamp", font_size=25).to_edge(DOWN + LEFT * 3)
        explanation_2_2 = Text("and the previous hash", font_size=25).next_to(explanation_2_1, RIGHT, buff=0.1)
        explanation_2 = VGroup(explanation_2_1, explanation_2_2)

        self.play(ReplacementTransform(explanation_1, explanation_2_1))
        self.next_slide()
        self.play(Write(prev_block_time))
        self.next_slide()

        # Shift the current block to the right
        self.play(bitcoin_block.animate.shift(RIGHT * 4), block_label.animate.shift(RIGHT * 4), block_info.animate.shift(RIGHT * 4))
        self.wait(0.5)

        left_block = Rectangle(width=6, height=4).set_fill(BLUE, opacity=0.3).move_to(LEFT * 4)
        left_block_label = Text("Previous Block", font_size=24).next_to(left_block, UP)
        self.play(Create(left_block), Write(left_block_label))
        self.wait(0.5)

        # Add the previous hash to the new block
        prev_timestamp = (datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
        prev_prev_block_hash = hashlib.sha256("Genesis Block".encode()).hexdigest()[:15] + "..."
        prev_block_info = VGroup(
            Text(f"Root Hash: {prev_block_hash}", font_size=25, color=ORANGE).move_to(left_block.get_center()),
            Text(f"Timestamp: {prev_timestamp}", font_size=25).next_to(left_block.get_center(), DOWN, buff=0.3),
        )
        self.play(Write(prev_block_info))
        self.next_slide()

        # Link the blocks as a chain
        prev_prev_block_hash = Text(f"Previous Block: {prev_prev_block_hash}", font_size=25).next_to(left_block.get_center(), DOWN, buff=0.9)
        prev_block_hash_text = Text(f"Previous Block: {prev_block_hash}", font_size=25).next_to(merkle_root, DOWN, buff=0.9)
        block_info.add(prev_block_hash_text)
        prev_block_info.add(prev_prev_block_hash)
        chain_link = Line(start=left_block.get_right(), end=bitcoin_block.get_left(), stroke_width=6, color=WHITE)
        self.play(Write(explanation_2_2))
        self.next_slide()

        self.play(Create(chain_link), Write(prev_prev_block_hash), Write(prev_block_hash_text))
        self.next_slide()
        self.play(FadeOut(block_info), FadeOut(prev_block_info), FadeOut(explanation_2), FadeOut(explanation_2_2), FadeOut(chain_link), FadeOut(bitcoin_block), FadeOut(left_block), FadeOut(block_label), FadeOut(left_block_label))
        self.next_slide()

        user_device = ImageMobject("bitcoin_user.png").scale(0.5).to_corner(LEFT)
        self.play(FadeIn(user_device))

        user_text = Text("User Verifying \n a Transaction", font_size=24).next_to(user_device, DOWN)
        self.play(Write(user_text))

        # Add Question Mark Next to User
        question_mark = Text("?", font_size=36, color=YELLOW).next_to(user_device, UP, buff=0.1)
        self.play(Write(question_mark))

        self.next_slide()

        # Bitcoin Image at the Center
        bitcoin_image = ImageMobject("bitcoin.png").scale(0.2).move_to(RIGHT * 3)

        # Network Representation: Nodes Around Bitcoin Image
        network_nodes = VGroup()
        angles = np.linspace(0, 2 * PI, 25, endpoint=False)
        radius = 2

        # Create Nodes Around Bitcoin Image
        for angle in angles:
            node = Dot(radius=0.1).set_color(BLUE).set_z_index(10)
            node.move_to(bitcoin_image.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0]))
            network_nodes.add(node)

        # Connect Nodes to Form a Network Graph
        network_lines = VGroup()
        for i, node in enumerate(network_nodes):
            next_node = network_nodes[(i + 1) % len(network_nodes)]
            line = Line(node.get_center(), next_node.get_center()).set_z_index(-1)
            network_lines.add(line)

        # Randomly connect nodes to form a network
        for i in range(35):
            node1 = random.choice(network_nodes)
            node2 = random.choice(network_nodes)
            line = Line(node1.get_center(), node2.get_center()).set_z_index(-1)
            network_lines.add(line)

        self.play(Create(network_nodes), Create(network_lines))
        self.play(FadeIn(bitcoin_image))

        self.next_slide()

        # Explanation Line
        explanation_1 = Text(
            "The user connects to the Bitcoin network to verify a specific transaction",
            font_size=25
        ).to_edge(DOWN)
        self.play(Write(explanation_1))
        self.next_slide()

        # Merkle Path to Root
        network_node = network_nodes[-10]
        path_line = DashedLine(user_device.get_right() + RIGHT * 0.5, network_node.get_center())
        self.play(network_node.animate.set_color(ORANGE), Create(path_line))
        self.next_slide()

        explanation_2 = Text(
            "The user requests a Merkle Proof from the network.",
            font_size=25
        ).to_edge(DOWN)
        self.next_slide()
        self.play(ReplacementTransform(explanation_1, explanation_2))
        self.next_slide()

        line = Line(path_line.get_start() + UP * 0.2, path_line.get_end() + UP * 0.2).set_opacity(0)
        transaction_hash = Text("TXN: 8a9f12...", font_size=18, color=BLUE).move_to(line.get_start())
        self.play(FadeIn(transaction_hash))
        self.play(MoveAlongPath(transaction_hash, line), run_time=2)
        self.play(FadeOut(transaction_hash))

        self.next_slide()
        explanation_3 = Text(
            "The node computes the Merkle Proof",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_2, explanation_3))

        self.play(FadeOut(path_line, network_node, bitcoin_image, user_text, user_device, question_mark, network_nodes, network_lines))
        self.next_slide()

        leaf_labels = ["h1", "h2", "h3", "h4"]
        leaf_nodes = VGroup()
        leaf_texts = VGroup()
        leaf_blocks = VGroup()
        x_positions = [-5, -2, 2, 5]

        for i, (label, x_pos) in enumerate(zip(leaf_labels, x_positions)):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(DOWN * 2.3 + RIGHT * x_pos)
            text = Text(label).scale(0.6)
            text.move_to(rect.get_center())
            leaf_nodes.add(rect)
            leaf_texts.add(text)
            leaf_blocks.add(VGroup(rect, text))

        parent_positions = [-3.5, 3.5]
        parent_nodes = VGroup()
        parent_texts = VGroup()
        parent_blocks = VGroup()

        for i in range(2):
            rect = Square(side_length=1.0, color=ORANGE)
            rect.shift(UP * 0.5 + DOWN + RIGHT * parent_positions[i])
            text = Text(f"h{i * 2 + 1}{i * 2 + 2}").scale(0.6)
            text.move_to(rect.get_center())
            parent_nodes.add(rect)
            parent_texts.add(text)
            parent_blocks.add(VGroup(rect, text))

        root_node = Square(side_length=1.2, color=ORANGE)
        root_node.shift(UP * 2.3 + DOWN)
        root_text = Text("h1234").scale(0.6)
        root_text.move_to(root_node.get_center())
        root_block = VGroup(root_node, root_text)

        # Create arrows
        arrows = VGroup()
        for i in range(2):
            left_arrow = Arrow(start=leaf_nodes[i * 2].get_top() + UP * 0.2,
                               end=parent_nodes[i].get_bottom() + LEFT * 0.3 + DOWN * 0.2, buff=0.1)
            right_arrow = Arrow(start=leaf_nodes[i * 2 + 1].get_top() + UP * 0.2,
                                end=parent_nodes[i].get_bottom() + RIGHT * 0.3 + DOWN * 0.2, buff=0.1)
            arrows.add(left_arrow, right_arrow)

        root_left_arrow = Arrow(start=parent_nodes[0].get_top() + UP * 0.2,
                                end=root_node.get_left() + LEFT * 0.2 + DOWN * 0.2, buff=0.1)
        root_right_arrow = Arrow(start=parent_nodes[1].get_top() + UP * 0.2,
                                 end=root_node.get_right() + RIGHT * 0.2 + DOWN * 0.2, buff=0.1)
        arrows.add(root_left_arrow, root_right_arrow)

        # Fade in the entire tree
        self.play(FadeIn(leaf_nodes), FadeIn(leaf_texts), FadeIn(parent_nodes), FadeIn(parent_texts), FadeIn(root_node),
                  FadeIn(root_text), FadeIn(arrows))
        self.next_slide()

        explanation_4 = Text(
            "This proof is a sequence of hashes needed to reconstruct the path \n from the transaction hash to the Merkle root.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_3, explanation_4))
        self.next_slide()

        self.play(Indicate(leaf_nodes[0], scale_factor=1.5))
        self.next_slide()
        explanation_5 = Text(
            "The transaction hash itself is not included in the proof.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_4, explanation_5))

        self.play(leaf_nodes[0].animate.set_color(YELLOW))
        self.next_slide()
        explanation_6 = Text(
            "Are included only the hashes of the sibling nodes along the path to the Merkle root.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_5, explanation_6))

        self.next_slide()
        self.play(leaf_nodes[1].animate.set_color(BLUE))
        self.next_slide()
        self.play(parent_nodes[1].animate.set_color(BLUE))
        self.next_slide()

        merkle_proof = VGroup(leaf_blocks[1].copy(), parent_blocks[1].copy()).arrange_in_grid(rows=1, buff=0.5)
        self.play(ReplacementTransform(VGroup(leaf_blocks, parent_blocks, root_block, arrows), merkle_proof))
        self.next_slide()

        merkle_proof_bullet = Dot(radius=0.1, color=BLUE).move_to(line.get_end())
        text = Text("The Merkle proof provides just enough information for you to \n compute the Merkle root starting from your transaction hash.", font_size=30, color=YELLOW).to_edge(LEFT)
        self.play(ReplacementTransform(merkle_proof, merkle_proof_bullet), Write(text))
        self.next_slide()

        reversed_line = Line(line.get_end(), line.get_start()).set_opacity(0)
        merkle_proof_text = Text("Merkle Proof", font_size=18, color=BLUE).move_to(reversed_line.get_start())

        explanation_7 = Text(
            "The server sends the Merkle Proof back to the user.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_6, explanation_7), FadeOut(text))
        self.next_slide()
        self.play(ReplacementTransform(merkle_proof_bullet, merkle_proof_text))

        self.play(FadeIn(path_line, network_node, bitcoin_image, user_text, user_device, question_mark, network_nodes, network_lines))

        self.play(MoveAlongPath(merkle_proof_text, reversed_line), run_time=2)
        self.play(FadeOut(merkle_proof_text))

        self.play(FadeOut(path_line, network_node, bitcoin_image, network_nodes, network_lines))
        self.next_slide()

        proof_blocks = VGroup()
        proof_labels = ["h1", "h2", "h34"]

        for i, label in enumerate(proof_labels):
            rect = Square(side_length=1.0, color=BLUE)
            text = Text(label).scale(0.6)
            text.move_to(rect.get_center())

            if i == 0:
                rect.set_color(YELLOW)

            proof_blocks.add(VGroup(rect, text))

        merkle_proof = proof_blocks.arrange_in_grid(rows=1, buff=0.5)
        merkle_proof.next_to(user_device, RIGHT * 2)
        self.play(FadeIn(VGroup(merkle_proof[1], merkle_proof[2])))
        self.next_slide()

        explanation_8 = Text(
            "The user combines the provided sibling hashes to reconstruct the Merkle Root.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_7, explanation_8))
        self.next_slide()

        leaf_group = VGroup(merkle_proof[0], merkle_proof[1])
        rect = Square(side_length=1.0, color=BLUE)
        text = Text("h12").scale(0.6)
        text.move_to(rect.get_center())
        parent_node = VGroup(rect, text).next_to(merkle_proof[2], LEFT)
        self.play(FadeIn(merkle_proof[0]))
        self.next_slide()

        self.play(ReplacementTransform(leaf_group, parent_node))
        self.next_slide()

        parent_group = VGroup(parent_node, merkle_proof[2])
        root_hash_text = Text("h1234:", color=BLUE).move_to(merkle_proof.get_center())
        root_hash_hash = Text("1e61a969e").next_to(root_hash_text, RIGHT, buff=0.1)
        root_hash = VGroup(root_hash_text, root_hash_hash)
        self.play(ReplacementTransform(parent_group, root_hash_text))
        self.next_slide()
        self.play(Write(root_hash_hash))
        self.next_slide()

        block_hash_test = Text("Block Hash:", color=ORANGE).next_to(root_hash_text, DOWN, buff=0.5)
        block_hash_hash = Text("1e61a969e").next_to(block_hash_test, RIGHT, buff=0.1)
        block_hash = VGroup(block_hash_test, block_hash_hash)
        self.play(Write(block_hash))
        self.next_slide()
        explanation_9 = Text(
            "The user compares the root hash with the hash in the block header.",
            font_size=25
        ).to_edge(DOWN)

        self.next_slide()
        self.play(ReplacementTransform(explanation_8, explanation_9))
        self.next_slide()
        self.play(Indicate(block_hash_hash, scale_factor=1.5), Indicate(root_hash_hash, scale_factor=1.5))

        self.next_slide()
        explanation_10 = Text(
            "The transaction is confirmed to be included in the block.",
            font_size=25
        ).to_edge(DOWN)

        check_mark = Text("✓", font_size=36, color=GREEN).move_to(question_mark.get_center())
        self.play(ReplacementTransform(explanation_9, explanation_10), ReplacementTransform(question_mark, check_mark))
        self.next_slide()

        self.play(FadeOut(explanation_10), FadeOut(check_mark), FadeOut(root_hash, block_hash), FadeOut(user_device, user_text))
        self.next_slide()


        # ########################################
        # #         Slide 12: Example Usage - DBMS
        #
        # # Transform the title
        # slide_12_title =  create_title("Example Usage - DBMS")
        # self.play(Transform(slide_11_title, slide_12_title, replace_mobject_with_target_in_scene=True))
        # self.next_slide()

        ########################################
        #         Slide 13: Benefits of Merkle Trees

        # Transform the title
        slide_13_title =  create_title("Benefits of Merkle Trees")
        self.play(Transform(slide_11_title, slide_13_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

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
            bullet.align_to(slide_13_title, LEFT)
            bullet.shift(UP * 2 + DOWN * (i * 0.6))
            bullet_points.add(bullet)

        for bullet in bullet_points:
            self.play(Write(bullet))
            self.next_slide()

        self.next_slide()

        self.play(FadeOut(bullet_points))
        self.next_slide()

        ########################################
        #         Slide 14: Take Home message

        # Transform the title
        slide_14_title =  create_title("Questions?").move_to(ORIGIN)
        self.play(Transform(slide_13_title, slide_14_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()

        ########################################
        #         Slide 15: Quiz Time

        # Transform the title
        slide_15_title = create_title("Quiz Time!").move_to(ORIGIN)
        self.play(Transform(slide_14_title, slide_15_title, replace_mobject_with_target_in_scene=True))
        self.next_slide()