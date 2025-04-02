# NOTE: Generated By HttpRunner v4.3.5
# FROM: .\testcase\dbsearch.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseDbsearch(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("movie_search")
            .get("https://search.douban.com/movie/subject_search")
            .with_params(**{"cat": "1002", "search_text": "liudehua"})
            .with_headers(
                **{
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
                    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
                    "sec-ch-ua-platform": '"Windows"',
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html")
        ),
    ]


if __name__ == "__main__":
    TestCaseDbsearch().test_start()
