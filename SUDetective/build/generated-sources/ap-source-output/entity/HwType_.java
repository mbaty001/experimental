package entity;

import entity.Lab;
import entity.Ms;
import entity.SuLog;
import entity.Ts;
import javax.annotation.Generated;
import javax.persistence.metamodel.ListAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.3.0.v20110604-r9504", date="2013-07-12T15:27:03")
@StaticMetamodel(HwType.class)
public class HwType_ { 

    public static volatile SingularAttribute<HwType, String> name;
    public static volatile ListAttribute<HwType, Ts> tsList;
    public static volatile ListAttribute<HwType, SuLog> suLogList;
    public static volatile ListAttribute<HwType, Ms> msList;
    public static volatile SingularAttribute<HwType, Integer> idHWTYPE;
    public static volatile ListAttribute<HwType, Lab> labList;

}