package entity;

import entity.Lab;
import entity.SuLog;
import entity.SuState;
import entity.SuType;
import javax.annotation.Generated;
import javax.persistence.metamodel.ListAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.3.0.v20110604-r9504", date="2013-07-12T15:27:03")
@StaticMetamodel(Su.class)
public class Su_ { 

    public static volatile SingularAttribute<Su, String> suStartTime;
    public static volatile SingularAttribute<Su, String> suEndTime;
    public static volatile SingularAttribute<Su, Lab> lABidLAB;
    public static volatile SingularAttribute<Su, Integer> idSU;
    public static volatile SingularAttribute<Su, String> suTo;
    public static volatile SingularAttribute<Su, SuState> sUSTATEidSUSTATE;
    public static volatile ListAttribute<Su, SuLog> suLogList;
    public static volatile SingularAttribute<Su, Integer> suErrors;
    public static volatile SingularAttribute<Su, String> suFrom;
    public static volatile SingularAttribute<Su, SuType> sUTYPEidSUTYPE;

}