Feature: Home Page

    Scenario: Any Name Test
        Given Open base url desktop view
        Then Open Page "/about"
        Then Validate current url with "/about"
        Then Click on "body > nav > div > div.collapse.navbar-collapse > ul > li:nth-child(1) > a", By "CSS_SELECTOR"
        Then Validate current title with "SWAPI - The Star Wars API"
