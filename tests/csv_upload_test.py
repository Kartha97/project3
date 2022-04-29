"""Test the csv songs upload"""

def test_csv(application, client):
    res = client.get("/songs/upload")
    print(res.data)
    assert res.status_code == 302
    upload_res = client.post("/songs/upload", data="/app/uploads/music.csv", follow_redirects=True)
    assert upload_res.status_code == 200