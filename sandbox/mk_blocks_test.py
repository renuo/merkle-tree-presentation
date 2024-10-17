from manim import *

class MerkleTreeBuildingBlocks(Scene):
    def construct(self):
        # Display the title
        title = Text("Building Blocks of Merkle Trees", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

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
            self.wait(0.2)

        self.wait(1)

        # Step 2: Transform data blocks into hash nodes
        hash_nodes = VGroup()
        hash_texts = VGroup()

        for i in range(4):
            # Transform the data block into a hash node with an orange border
            hash_rect = Square(side_length=1.0, color=ORANGE)
            hash_rect.move_to(leaf_nodes[i].get_center())
            hash_label = Text(f"h{i+1}").scale(0.6)
            hash_label.move_to(hash_rect.get_center())

            # Add to groups
            hash_nodes.add(hash_rect)
            hash_texts.add(hash_label)

            # Animate the transformation
            self.play(Transform(leaf_nodes[i], hash_rect), Transform(leaf_texts[i], hash_label))
            self.wait(0.2)

        self.wait(1)

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
            self.wait(1)

            self.play(left_child_copy.animate.move_to(RIGHT * (parent_positions[i] - 0.2)),
                      right_child_copy.animate.move_to(RIGHT * (parent_positions[i] + 0.2)))
            self.wait(0.5)

            self.play(Create(rect))
            self.wait(0.2)

        self.wait(1)

        for i in range(2):
            # Transform the data block into a hash node with an orange border
            hash_rect = Square(side_length=1.0, color=ORANGE)
            hash_rect.move_to(parent_hash_nodes[i].get_center())
            hash_label = Text(f"h{i*2+1}{i*2+2}").scale(0.6)
            hash_label.move_to(hash_rect.get_center())

            # Add to groups
            hash_nodes.add(hash_rect)
            hash_texts.add(hash_label)

            # Animate the transformation
            self.play(Transform(parent_hash_nodes[i], hash_rect), Transform(parent_hash_texts[i], hash_label))
            parent_hash_nodes[i] = hash_rect
            parent_hash_texts[i] = hash_label

            self.wait(0.2)


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
        # Animate concatenation and hashing for root
        left_parent_copy = parent_hash_texts[0].copy()
        right_parent_copy = parent_hash_texts[1].copy()
        self.play(Create(left_arrow), Create(right_arrow))
        self.wait(1)

        self.play(left_parent_copy.animate.move_to(UP * 3 + DOWN + LEFT * 0.3),
                  right_parent_copy.animate.move_to(UP * 3 + DOWN + RIGHT * 0.3))

        root_text = VGroup(left_parent_copy, right_parent_copy)

        self.wait(0.5)
        self.play(Create(root_node))
        self.wait(1)

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

        # Final wait
        self.wait(2)

if __name__ == "__main__":
    import os
    os.system("manim -qm -p mk_blocks_test.py MerkleTreeBuildingBlocks")