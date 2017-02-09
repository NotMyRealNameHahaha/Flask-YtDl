import unittest
import json
import YTR
from urllib.parse import urlparse


class FlaskTubeTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = YTR.app.test_client()
        self.app.testing = True

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_home_status_code(self):
        """
            Hit index() with a GET request
        """
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)
        assert b'YTR' in result.data

    def test_home_post_status_code(self):
        # Let's download some death metal... for testing, obviously
        ddict = {"input_id": "test_input_id", "input_value": "https://www.youtube.com/watch?v=zvEWFjWfqiU"}
        post_req = self.app.post("/", data=json.dumps(ddict), follow_redirects=False)
        assert b'test_input_id' in post_req.data

    def test_url_checker_post_request(self):
        vid_request = {"input_id": "test_input_id",
                       "input_value": "https://www.youtube.com/watch?v=zvEWFjWfqiU"}
        vid_response = {"input_id": "test_input_id", "video_name": "Heavy Metal Cats"}
        post_req = self.app.post("/checker", data=json.dumps(vid_request), follow_redirects=True)
        print(post_req.data)
        self.assertEqual(json.loads(post_req.data), vid_response)

    def test_song_get_request(self):
        result = self.app.get("/songs")
        self.assertEqual(result.status_code, 200)

    def test_song_post_request(self):
        test_key = urlparse("Heavy Metal Cats")
        song_post = self.app.post("/songs", data={test_key: "no"}, follow_redirects=True)
        self.assertEqual(song_post.status_code, 200)
