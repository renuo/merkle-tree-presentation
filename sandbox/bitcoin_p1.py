import datetime
import hashlib

from manim import *


class BitcoinTransactionsBlock(Scene):
    def construct(self):
        # Scene: Bitcoin Transactions in a Block
        title = Text("Bitcoin Transactions in a Block", font_size=36, weight=BOLD).to_edge(UP)
        self.play(Write(title))

        # Create a block representing a container labeled "Bitcoin Block"
        bitcoin_block = Rectangle(width=6, height=4).set_fill(BLUE, opacity=0.3)
        block_label = Text("Bitcoin Block", font_size=24).next_to(bitcoin_block, UP)
        self.play(Create(bitcoin_block), Write(block_label))
        self.wait(1)

        # Create a matrix of transactions inside the block
        transactions = VGroup(*[Text(f"Tx {i + 1}", font_size=20) for i in range(16)])
        transactions.arrange_in_grid(rows=4, buff=0.7).move_to(bitcoin_block.get_center())
        self.play(ShowIncreasingSubsets(transactions))
        self.wait(2)

        transaction_hashes = VGroup()
        for i in range(16):
            tx_hash = hashlib.sha256(f"Tx {i + 1}".encode()).hexdigest()[:5]
            hash_text = Text(f"{tx_hash}..", font_size=20, color=ORANGE)
            transaction_hashes.add(hash_text)
        transaction_hashes.arrange_in_grid(rows=4, buff=0.7).move_to(bitcoin_block.get_center())
        self.play(ReplacementTransform(transactions, transaction_hashes))
        self.wait(2)

        combined_hash_input = ''.join([hashlib.sha256(f"Tx {i + 1}".encode()).hexdigest() for i in range(16)])
        merkle_root_hash = hashlib.sha256(combined_hash_input.encode()).hexdigest()[:15]
        merkle_root = Text(f"Root Hash: {merkle_root_hash}...", font_size=25, color=ORANGE).move_to(bitcoin_block.get_center())
        self.play(ReplacementTransform(transaction_hashes, merkle_root))
        self.wait(1)

        # Add text explaining the Merkle root
        explanation_1 = Text("Merkle root summarizes all the transactions in a block", font_size=25).to_edge(DOWN)
        self.play(Write(explanation_1))
        self.wait(2)

        # Add basic information below the block after explanation
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prev_block_hash = hashlib.sha256("Previous Block".encode()).hexdigest()[:15] + "..."
        prev_block_time = Text(f"Timestamp: {timestamp}", font_size=25).next_to(merkle_root, DOWN, buff=0.3)
        block_info = VGroup(prev_block_time, merkle_root)

        explanation_2_1 = Text("Blocks contain other important information like timestamp", font_size=25).to_edge(DOWN + LEFT * 3)
        explanation_2_2 = Text("and the previous hash", font_size=25).next_to(explanation_2_1, RIGHT, buff=0.1)
        explanation_2 = VGroup(explanation_2_1, explanation_2_2)

        self.play(ReplacementTransform(explanation_1, explanation_2_1))
        self.wait(1)
        self.play(Write(prev_block_time))
        self.wait(1)

        # Shift the current block to the right
        self.play(bitcoin_block.animate.shift(RIGHT * 4), block_label.animate.shift(RIGHT * 4), block_info.animate.shift(RIGHT * 4))
        self.wait(1)

        left_block = Rectangle(width=6, height=4).set_fill(BLUE, opacity=0.3).move_to(LEFT * 4)
        left_block_label = Text("Previous Block", font_size=24).next_to(left_block, UP)
        self.play(Create(left_block), Write(left_block_label))
        self.wait(1)

        # Add the previous hash to the new block
        prev_timestamp = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        prev_prev_block_hash = hashlib.sha256("Genesis Block".encode()).hexdigest()[:15] + "..."
        prev_block_info = VGroup(
            Text(f"Hash: {prev_block_hash}", font_size=25, color=ORANGE).move_to(left_block.get_center()),
            Text(f"Timestamp: {prev_timestamp}", font_size=25).next_to(left_block.get_center(), DOWN, buff=0.3),
        )
        self.play(Write(prev_block_info))
        self.wait(2)

        # Link the blocks as a chain
        prev_prev_block_hash = Text(f"Previous Block: {prev_prev_block_hash}", font_size=25).next_to(left_block.get_center(), DOWN, buff=0.9)
        prev_block_hash_text = Text(f"Previous Block: {prev_block_hash}", font_size=25).next_to(merkle_root, DOWN, buff=0.9)
        explanation_3 = Text("Blocks contain other important information like timestamp and the previous hash", font_size=25).to_edge(DOWN)
        block_info.add(prev_block_hash_text)
        prev_block_info.add(prev_prev_block_hash)
        chain_link = Line(start=left_block.get_right(), end=bitcoin_block.get_left(), stroke_width=6, color=WHITE)
        self.play(Create(chain_link), Write(prev_prev_block_hash), Write(prev_block_hash_text), Write(explanation_2_2))
        self.wait(2)

        # Hold the final frame
        self.wait(2)

if __name__ == "__main__":
    import os

    os.system("manim -qm -p bitcoin.py BitcoinTransactionsBlock")
