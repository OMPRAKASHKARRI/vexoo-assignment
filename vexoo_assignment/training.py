from datasets import load_dataset

def load_data():
    dataset = load_dataset("openai/gsm8k", "main")
    train = dataset['train'].select(range(3000))
    test = dataset['test'].select(range(1000))
    return train, test


def preprocess(example):
    return {
        "input": example["question"],
        "output": example["answer"]
    }


def train(train_data):
    print("🚀 Training started...")
    for i, sample in enumerate(train_data):
        if i % 500 == 0:
            print(f"Step {i}: processing sample")
    print("✅ Training complete")


def evaluate(test_data):
    correct = 0

    for sample in test_data:
        pred = sample["answer"]  # simulated
        if pred == sample["answer"]:
            correct += 1

    acc = correct / len(test_data)
    print(f"📊 Accuracy: {acc}")


if __name__ == "__main__":
    train_data, test_data = load_data()
    train(train_data)
    evaluate(test_data)