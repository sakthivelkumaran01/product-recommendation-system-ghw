import pandas as pd


data = {
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3],
    "product_id": [101, 102, 103, 101, 104, 102, 103, 104],
    "rating": [5, 3, 4, 4, 5, 4, 5, 3]
}

df = pd.DataFrame(data)

user_item_matrix = df.pivot_table(
    index="user_id",
    columns="product_id",
    values="rating"
)

product_avg_ratings = user_item_matrix.mean()


def recommend_products(user_id, top_n=2):
    if user_id not in user_item_matrix.index:
        return "User not found"

    rated_products = user_item_matrix.loc[user_id].dropna().index
    recommendations = product_avg_ratings.drop(rated_products)

    return recommendations.sort_values(ascending=False).head(top_n)

user_id = 1
recommended_products = recommend_products(user_id)

print(f"Recommended products for User {user_id}:")
print(recommended_products)
