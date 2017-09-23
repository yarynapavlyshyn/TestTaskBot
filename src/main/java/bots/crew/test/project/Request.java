package bots.crew.test.project;

import bots.crew.test.project.Imp.IRequest;

import java.util.Scanner;

public class Request implements IRequest {

    // default action is to add
    public Action action;
    public String author;
    public String bookName;
    public String newBookName;

    public Request(String _request) throws Exception {
        String[] request = _request.split(" ");

        // verifying action
        String toDo = request[0];

        if (toDo.equals("all")) {
            action = Action.SHOWaLL;
            return;
        }

        if (toDo.equals("remove")) {
            action = Action.REMOVE;
            bookName = "" + '"';
            for (int i = 1; i < request.length; i++)
                bookName += request[i];
            bookName += "" + '"';
            return;
        }

        if (toDo.equals("edit")) {
            action = Action.EDIT;
            bookName = "" + '"';
            for (int i = 1; i < request.length; i++)
                bookName += request[i];
            bookName += "" + '"';
            System.out.println("PLease, type a new name:");
            Scanner sc = new Scanner(System.in);
            newBookName = sc.nextLine();
            return;
        }

        if (toDo.equals("add")) {
            action = Action.ADD;
            // verifying author
            author = request[1];
            int i = 2;
            while (!request[i].startsWith("" + '"')) {
                author += " " + request[i];
                i++;
            }
            // verifying book name
            bookName = "";
            while (i < request.length) {
                bookName += request[i];
                i++;
            }
            return;
        }

        throw new Exception("Sorry, we do not know how to perform your request. " +
                "Try again please.");
    }

    public String getBookName() {
        return bookName;
    }

    public String getAuthor() {
        return author;
    }

    public Action getAction() {
        return action;
    }

    public String getNewBookName() {
        return newBookName;
    }
}
