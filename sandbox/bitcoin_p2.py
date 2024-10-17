import random
from tkinter.constants import BOTTOM
from tkinter.tix import Select

from manim import *


class BitcoinTransactionsBlock(Scene):
    def construct(self):
        # Scene: Bitcoin Transactions in a Block
        title = Text("Bitcoin Transactions in a Block", font_size=36, weight=BOLD).to_edge(UP)
        self.play(Write(title))

        user_device = ImageMobject("bitcoin_user.png").scale(0.5).to_corner(LEFT)
        self.play(FadeIn(user_device))

        user_text = Text("User Verifying \n a Transaction", font_size=24).next_to(user_device, DOWN)
        self.play(Write(user_text))

        # Add Question Mark Next to User
        question_mark = Text("?", font_size=36, color=YELLOW).next_to(user_device, UP, buff=0.1)
        self.play(Write(question_mark))

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

        # Explanation Line
        explanation_1 = Text(
            "Device connects to the Bitcoin network to verify a specific transaction",
            font_size=25
        ).to_edge(DOWN)
        self.play(Write(explanation_1))

        # Merkle Path to Root
        network_node = network_nodes[-10]
        self.play(network_node.animate.set_color(ORANGE))

        explanation_2 = Text(
            "The user's device requests a Merkle Proof from the network.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_1, explanation_2))

        path_line = DashedLine(user_device.get_right() + RIGHT * 0.5, network_node.get_center())
        self.play(Create(path_line))

        line = Line(path_line.get_start() + UP * 0.2, path_line.get_end() + UP * 0.2).set_opacity(0)
        transaction_hash = Text("TXN: 8a9f12...", font_size=18, color=BLUE).move_to(line.get_start())
        self.play(MoveAlongPath(transaction_hash, line), run_time=2)
        self.play(FadeOut(transaction_hash))
        self.wait(1)
        explanation_3 = Text(
            "The node computes the Merkle Proof",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_2, explanation_3))

        self.play(FadeOut(path_line, network_node, bitcoin_image, user_text, user_device, question_mark, network_nodes, network_lines))
        self.wait(1)

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
        self.wait(1)

        explanation_4 = Text(
            "This proof is a sequence of hashes needed to reconstruct the path \n from the transaction hash to the Merkle root.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_3, explanation_4))

        self.play(Indicate(leaf_nodes[0], scale_factor=1.5))
        self.wait(1)
        explanation_5 = Text(
            "The transaction hash itself is not included in the proof.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_4, explanation_5))

        self.play(leaf_nodes[0].animate.set_color(YELLOW))
        self.wait(1)
        explanation_6 = Text(
            "Are included only the hashes of the sibling nodes along the path to the Merkle root.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_5, explanation_6))

        self.wait(1)
        self.play(leaf_nodes[1].animate.set_color(BLUE))
        self.wait(1)
        self.play(parent_nodes[1].animate.set_color(BLUE))

        merkle_proof = VGroup(leaf_blocks[1].copy(), parent_blocks[1].copy()).arrange_in_grid(rows=1, buff=0.5)
        self.play(ReplacementTransform(VGroup(leaf_blocks, parent_blocks, root_block, arrows), merkle_proof))

        merkle_proof_bullet = Dot(radius=0.1, color=BLUE).move_to(line.get_end())
        text = Text("The Merkle proof provides just enough information for you to \n compute the Merkle root starting from your transaction hash.", font_size=30, color=YELLOW).to_edge(LEFT)
        self.play(ReplacementTransform(merkle_proof, merkle_proof_bullet), Write(text))
        self.wait(1)

        reversed_line = Line(line.get_end(), line.get_start()).set_opacity(0)
        merkle_proof_text = Text("Merkle Proof", font_size=18, color=BLUE).move_to(reversed_line.get_start())

        explanation_7 = Text(
            "The server sends the Merkle Proof back to the user's device.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_6, explanation_7), ReplacementTransform(merkle_proof_bullet, merkle_proof_text))
        self.wait(1)

        self.play(FadeOut(text), FadeIn(path_line, network_node, bitcoin_image, user_text, user_device, question_mark, network_nodes, network_lines))
        self.wait(1)

        self.play(MoveAlongPath(merkle_proof_text, reversed_line), run_time=2)
        self.play(FadeOut(merkle_proof_text))

        self.play(FadeOut(path_line, network_node, bitcoin_image, network_nodes, network_lines))
        self.wait(1)

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
        self.wait(1)

        explanation_8 = Text(
            "The user combines the provided sibling hashes to reconstruct the Merkle Root.",
            font_size=25
        ).to_edge(DOWN)
        self.play(ReplacementTransform(explanation_7, explanation_8))
        self.wait(1)

        leaf_group = VGroup(merkle_proof[0], merkle_proof[1])
        rect = Square(side_length=1.0, color=BLUE)
        text = Text("h12").scale(0.6)
        text.move_to(rect.get_center())
        parent_node = VGroup(rect, text).next_to(merkle_proof[2], LEFT)
        self.play(FadeIn(merkle_proof[0]))
        self.wait(1)

        self.play(ReplacementTransform(leaf_group, parent_node))
        self.wait(1)

        parent_group = VGroup(parent_node, merkle_proof[2])
        root_hash_text = Text("Merkle Root: ").move_to(merkle_proof.get_center())
        root_hash_hash = Text("1e61a969e").next_to(root_hash_text, RIGHT, buff=0.1)
        root_hash = VGroup(root_hash_text, root_hash_hash)
        self.play(ReplacementTransform(parent_group, root_hash))

        block_hash_test = Text("Block Hash:").next_to(root_hash, DOWN, buff=0.5)
        block_hash_hash = Text("1e61a969e").next_to(block_hash_test, RIGHT, buff=0.1)
        block_hash = VGroup(block_hash_test, block_hash_hash)
        self.play(Write(block_hash))

        self.wait(1)
        explanation_9 = Text(
            "The user compares the root hash with the hash in the block header",
            font_size=25
        ).to_edge(DOWN)
        self.play(Indicate(block_hash_hash, scale_factor=1.5), Indicate(root_hash_hash, scale_factor=1.5), ReplacementTransform(explanation_8, explanation_9))

        self.wait(1)
        explanation_10 = Text(
            "If the hashes match, the transaction is confirmed to be included in the block.",
            font_size=25
        ).to_edge(DOWN)

        check_mark = Text("✓", font_size=36, color=GREEN).move_to(question_mark.get_center())
        self.play(ReplacementTransform(explanation_9, explanation_10), ReplacementTransform(question_mark, check_mark))
        self.wait(1)

        self.play(FadeOut(explanation_10), FadeOut(check_mark), FadeOut(root_hash, block_hash), FadeOut(user_device, user_text))
        self.wait(1)




if __name__ == "__main__":
    import os
    # os.system("open /Users/gianlo_work/Develop/lw-24-slides/sandbox/media/videos/bitcoin_p2/720p30/BitcoinTransactionsBlock.mp4")
    os.system("manim -qm -p bitcoin_p2.py BitcoinTransactionsBlock")
