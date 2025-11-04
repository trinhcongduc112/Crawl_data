---
title: Tasks
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: basic
      slug: how-to-create-an-action
      title: How to create an Action
    - type: basic
      slug: how-to-create-a-task
      title: How to create a Task
---
<Image title="2c7ecad-SMART-goals.png" alt={792} src="https://files.readme.io/6a56dd8-2c7ecad-SMART-goals.png">
  SMART Goals for any Abivin vRoute Task.
</Image>

## Tasks

We are big fans of SMART goals (Specific, Measurable, Attainable, Relevant, Time Based) that we want to spread this to our customers. Without a specific description, a person doesn’t know what he need to do. Even if he knows what to do, he still needs to know what measures his success for him to focus. Lastly, without setting a goal time-bounded, someone can just do everything right, forever and achieve nothing, in the end.

Therefore, we want to implement the SMART goals into vRoute’s tasks. A vRoute task is the central core of vRoute system. The requirements for a vRoute task to exist are the components we have defined above: Users, Customers, Products. These are the reasons to have a task. For example, Nga has a task of calculating the salary of everyone in October - due by noon of the first Tuesday in November or Dang has a task of complete front-end, back-end integration for module Action, to be completed in 8 hours.

Goals:

* A user has to complete a series of tasks
* Tasks has to be defined clearly with an Action
* Tasks are grouped in Projects to display the progress over time: what has to be done urgently and importantly, what can be left to next week
* Tasks are grouped into Actions to display the actual activities to be done

## Actions

Action defines the "Form" of a Task. A Task can be assigned to only a single Action; a Task can just simply have description of how someone can do it and be marked status with “In progress” or “Done”. However, if we want users to do more specific work to complete a task, we select Actions for it to be completed. An Action can be customized into Questios-Answer pairs. We store the Question-Answer database in an EAV (Entity-Attribute-Value) relationship. In other words, EAV of (X, Y, Z) means Entity X’s attribute Y is assigned value Z. This is used when the attribute of Y is very sparse and we don’t want to corporate that into model of X.

We build a collection of Attributes when creating/updating an Action.

When list all tasks of one user, if this is user:

* Admin: able to view all of the resources belonging to its organization and descendants
* User X:
* Read self:\
  **Able to view tasks where X is assigned to\&#xA;** Able to view tasks where X creates itself
* Read\_all:\
  \*\* Able to view tasks from its organization and descendants

An Action can be built using our advanced Form Builder.

## Form Builder

Forms helps us to define the details of Actions. Via Forms, we are able to define every box of information: e.g. check box, item list, text field. The form can be defined in a drag and drop manner.
