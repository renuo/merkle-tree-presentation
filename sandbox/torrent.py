from manim import *

class MerkleTreeTorrentDemo(Scene):
    def construct(self):
        title = Text(
            "Torrent example",
            weight=BOLD
        ).to_edge(UP)
        self.play(Write(title))

        label_1 = Text("1. Retrieve file metadata", color=YELLOW).to_edge(DOWN)
        self.play(Write(label_1))

        # Animation 1: Large File with a Hash
        file_box = Square().scale(1.5).set_fill(BLUE, opacity=0.5)
        file_label = Text("File.mkv 30GB").next_to(file_box, UP)
        file_hash = Text("Merkle Root: f2f5f5426").next_to(file_box, DOWN)
        self.play(Create(file_box), Write(file_label), Write(file_hash))
        self.wait(1)

        label_2 = Text("2. Get chunks from seeds", color=YELLOW).to_edge(DOWN)
        self.play(ReplacementTransform(label_1, label_2))

        chunks = VGroup(*[Square().scale(0.5).set_fill(BLUE, opacity=0.5) for _ in range(4)])
        chunks.arrange_in_grid(rows=1, buff=0.5).next_to(title, DOWN, buff=2)

        chunk_labels = VGroup(*[Text(f"C{i+1}").next_to(chunks[i], DOWN) for i in range(4)])

        self.play(ReplacementTransform(file_box, chunks), Write(chunk_labels), FadeOut(file_label), FadeOut(file_hash))
        self.wait(1)

        label_3 = Text("3. Download Chunks", color=YELLOW).to_edge(DOWN)
        self.play(ReplacementTransform(label_2, label_3))
        self.wait(1)

        chunk_hashes = VGroup(*[Text(f"H{i+1}").next_to(chunks[i], DOWN).set_color(ORANGE) for i in range(4)])

        for i in [3, 0, 2, 1]:
            self.play(chunks[i].animate.set_fill(GREEN, opacity=0.7), run_time=1)
            self.wait(0.5)

        label_4 = Text("4. Compute Merkle Tree", color=YELLOW).to_edge(DOWN)
        self.play(ReplacementTransform(label_3, label_4))
        self.wait(1)

        for i in range(4):
            self.play(chunks[i].animate.set_fill(ORANGE, opacity=0.7), run_time=1)
            self.play(ReplacementTransform(chunk_labels[i], chunk_hashes[i]))
            self.wait(0.5)

        self.wait(1)

        merkle_root_text = Text("H1234:", color=ORANGE).move_to(ORIGIN + LEFT)
        self.play(ReplacementTransform(chunks, merkle_root_text), FadeOut(chunk_hashes))
        self.wait(1)

        merkle_root_hash = Text("f2f5f5426", color=ORANGE).next_to(merkle_root_text, RIGHT)
        merkle_root_group = VGroup(merkle_root_text, merkle_root_hash)
        self.play(Write(merkle_root_group))
        self.wait(1)


        label_5 = Text("5. Compare Root Hash", color=YELLOW).to_edge(DOWN)
        self.play(ReplacementTransform(label_4, label_5))
        self.wait(1)

        file_text = Text("Merkle Root:").next_to(merkle_root_text, DOWN)
        file_hash = Text("f2f5f5426").next_to(file_text, RIGHT)
        file_text_group = VGroup(file_text, file_hash)

        self.play(Write(file_text_group))
        self.wait(1)

        label_6 = Text("File Integrity Verified!", color=GREEN).to_edge(DOWN)
        self.play(Indicate(file_hash, scale_factor=1.2, color=GREEN), Indicate(merkle_root_hash, scale_factor=1.2, color=GREEN))
        self.play(ReplacementTransform(label_5, label_6))
        self.wait(2)

        # Clear the scene
        self.play(FadeOut(VGroup(merkle_root_group, file_text_group, label_6, title)))
        self.wait(1)


if __name__ == "__main__":
    import os
    os.system("manim -qm -p torrent.py MerkleTreeTorrentDemo")