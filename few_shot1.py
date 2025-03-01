import pandas as pd # FAKE
import json

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                posts = json.load(f)
                self.df = pd.json_normalize(posts)
                self.df["length"] = self.df["line_count"].apply(self.categorize_length)
                all_tags = self.df["tags"].apply(lambda x: x).sum()
                self.unique_tags = set(list(all_tags))
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        if self.df is not None:
            df_filtered = self.df[
                (self.df['language'] == language) &
                (self.df['length'] == length) &
                (self.df['tags'].apply(lambda tags: tag in tags))
            ]
            return df_filtered.to_dict(orient="records")
        else:
            return []

if __name__ == "__main__":
    fs = FewShotPosts()
    if fs.df is not None:
        print("Data loaded successfully.")
        print(fs.get_tags())
    else:
        print("Failed to load data.")
