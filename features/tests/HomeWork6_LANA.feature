# Created by Limit at 11/9/2022
Feature: Homework Open New Window


Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 And Store original windows
 When Click on Amazon Privacy Notice link
 And Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 And User can close new window and switch back to original