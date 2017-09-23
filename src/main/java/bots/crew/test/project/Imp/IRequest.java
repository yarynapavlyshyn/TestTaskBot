package bots.crew.test.project.Imp;

import bots.crew.test.project.Action;

public interface IRequest {
    String getAuthor();
    String getBookName();
    String getNewBookName();
    Action getAction();
}
