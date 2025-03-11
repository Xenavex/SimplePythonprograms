# ==========================================================
#  Name : Youtube Playlist Video Status Checker ( YPVSC )
#  IGN : Xenavex | Hatakechop3
#  Discord : 𝐗𝐞𝐧𝐚𝐯𝐞𝐱
#  Twitter : @Xenavex
#  Website : Bit.ly/Hatakeall
# ==========================================================
#  Code Made in Help With ChatGPT
# ==========================================================

# Importing Google API Package
from googleapiclient.discovery import build

# Section 1 of 5 : Input Of Youtube Data API | Playlist ID  & Initialization Of Script ( Hardcoding & Dynamic Input of Both API & Playlist ID & Error Correction is Supported )

# Input Of API
API_KEY = ""
# API_KEY = input("Enter the API KEY: ") ( Manual Input if required )

# Input Of the Playlist ID
playlist_id = input("Enter the playlist ID: ").strip()
# playlist_id = ""( Auto Input if required )

# Checks if the "playlist_id" contains The YouTube URL instead of only the playlist ID ( Error Correction )
if "youtube.com" in playlist_id or "list=" in playlist_id:
    print("Error: Please enter only the Playlist ID, not the full URL [It is the random string of characters after https://www.youtube.com/playlist?list= ]")
    exit()

# Initialising The API
youtube = build('youtube', 'v3', developerKey=API_KEY)

print("Section 1 of 5 Completed")

# Section 2 of 5 : Retrieval and Storage of Video ID's ( Pagination if >50 videos ) 

def get_playlist_items(playlist_id):
    video_ids = []
    next_page_token = None

    # While True Loop that Retrieves Video Details ( content details ) 
    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )

        response = request.execute()

        # Collection & Storage OF Video ID'S
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        
        # Checks if There are any remaining videos left to retrive the ID ( If "next_page_token" is present the loop continues otherwise it breaks )
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    print("Section 2 of 5 Completed")
    return video_ids

# Section 3 of 5 : Checks the status of the videos retrieved & Handles Errors

# Interacts with the API to Check the Status of the Video and Add it to a List
def check_video_status(video_id):
    try:
        request = youtube.videos().list(
            part="status",
            id=video_id
        )   
        response = request.execute()

        if not response['items']:
            return f"Video ID {video_id}: Deleted or not found"
        # Checks if a video is viewable or restricted 
        try:
            status = response['items'][0]['status']
            if status['privacyStatus'] == "public":
                return "Public"
            elif status['privacyStatus'] == "unlisted":
                return f"Video ID {video_id}: Unlisted"
            elif status['privacyStatus'] == "private":
                return f"Video ID {video_id}: Private"
        # Error Catching ( If Weird Errors are encountered it Displays the Error Received along with the Video ID )
        except KeyError:
            return f"Video ID {video_id}: Error - Missing 'status' key in response"
        except TypeError:
            return f"Video ID {video_id}: Error - Response is not iterable"
    # Prevents crashes and ensures errors are logged | Printed
    except Exception as e:
        return f"Video ID {video_id}: API Request Failed - {str(e)}"

# Takes the List that contains the ID & Status and Filters out Available Videos and Keeps the Rest ( Unviewable Videos are Added to the List)
def check_all_video_status(video_ids):
    unviewable_videos = []
    for video_id in video_ids:
        status = check_video_status(video_id)
        if "Error" in status or status in ["Unlisted", "Private", f"Video ID {video_id}: Deleted or not found"]:
            unviewable_videos.append(f"{video_id} is unviewable")
    print("Section 3 of 5 Completed") 
    return unviewable_videos

# Section 4 of 5 : Retrives the ID From the list that contains Unviewable Videos and Prints them along with any Errors with the ID of Said Video
def main():
    video_ids = get_playlist_items(playlist_id)
    unviewable_videos = check_all_video_status(video_ids)

    # Printing Non-Public Video IDs
    if unviewable_videos:
        for video in unviewable_videos:
            print()
            print("The Following Videos are Unavailable")
            print(video)
            print()
    else:
        print("All videos are viewable")

    print("Section 4 of 5 Completed")

# Section 5 of 5 : Safety Measures & Exit

if __name__ == "__main__":
    main()
    print("Section 5 of 5 Completed")

# Exit
input("Enter to exit")

# End Of Code