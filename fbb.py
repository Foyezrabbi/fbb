import time
import facebook

# Replace with your access tokens
source_group_access_token = "your-source-group-access-token"
target_group_access_token = "your-target-group-access-token"

# Replace with the IDs of the source and target groups
source_group_id = "your-source-group-id"
target_group_id = "your-target-group-id"

# Initialize the Facebook Graph API using the access tokens
graph = facebook.GraphAPI(access_token=source_group_access_token, version="3.0")

# Initialize the Facebook Graph API using the access tokens for the target group
target_graph = facebook.GraphAPI(access_token=target_group_access_token, version="3.0")

# Keep track of the last post ID that was processed
last_post_id = None

while True:
    # Get the latest posts from the source group
    posts = graph.get_connections(source_group_id, "feed")

    # Process each post in reverse chronological order
    for post in reversed(posts["data"]):
        post_id = post["id"]
        if post_id != last_post_id:
            # This is a new post, so share it to the target group
            message = post.get("message", "")
            link = post.get("link", "")
            picture = post.get("picture", "")

            target_graph.put_object(target_group_id, "feed", message=message, link=link, picture=picture)

            # Update the last post ID
            last_post_id = post_id

    # Wait for some time before checking for new posts again
    time.sleep(60)  # Wait for 60 seconds
